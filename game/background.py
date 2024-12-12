from pico2d import *
import random
import gfw
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Background(gfw.Sprite):
    IMAGE_MAG = 2  # 이미지 확대율
    # 키 맵핑: 키 입력과 이동 방향을 매핑
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): 1,
        (SDL_KEYDOWN, SDLK_RIGHT): -1,
        (SDL_KEYUP, SDLK_LEFT): -1,
        (SDL_KEYUP, SDLK_RIGHT): 1
    }
    SPEED_KEY_MAP = {
        (SDL_KEYDOWN, SDLK_a): 1,  # 속력 증가
        (SDL_KEYUP, SDLK_a): 0,  # 속력 유지
        (SDL_KEYDOWN, SDLK_s): -1,  # 속력 감소
        (SDL_KEYUP, SDLK_s): 0,  # 속력 유지
    }
    MAX_ROLL = 0.4  # 최대 롤 값

    def __init__(self):
        super().__init__(resource_path('res/roads/road1_1.png'), get_canvas_width() // 2, get_canvas_height() // 2)
        self.dx = 0
        self.speed = 0
        self.dspeed = 0
        self.width = self.image.w * Background.IMAGE_MAG
        self.height = self.image.h * Background.IMAGE_MAG
        self.min_x = get_canvas_width() // 4
        self.max_x = (get_canvas_width() // 4) * 3
        self.roll_time = 0
        self.fuel = 1000
        self.score = 0
        self.roadCheck = 100
        self.roadMove = 0

        self.engine = gfw.sound.sfx(resource_path("res/sound/engine.wav"))

        # 이미지 시리즈 로드
        self.images = []
        for j in range(1, 5):
            image_path = resource_path(f'res/roads/road4_{j}.png')  # 경로 수정
            self.images.append(load_image(image_path))

        # 현재 도로 인덱스 초기화
        self.current_road_index = 4
        self.current_image_index = 0
        self.image_change_speed = 1
        self.frame_count = 0

    def get_center_x(self):
        return self.x

    def handle_event(self, e):
        pair = (e.type, e.key)

        if pair in Background.KEY_MAP:
            self.dx += Background.KEY_MAP[pair]
        elif pair in Background.SPEED_KEY_MAP and self.fuel > 0:
            self.dspeed = Background.SPEED_KEY_MAP[pair]

            if e.type == SDL_KEYDOWN and e.key == SDLK_a:
                self.engine.play()

        if e.key == SDLK_9:
            self.score = 10000
        if e.key == SDLK_0:
            self.fuel = 0

    def update(self):
        if self.roadCheck < self.score:
            if self.roadCheck % 1000 == 0 and self.score != 0:
                self.fuel += 50
                if self.fuel > 1000:
                    self.fuel = 1000

            self.roadCheck += 50
            self.current_road_index += random.randint(-1, 1)

            if self.current_road_index < 1:
                self.current_road_index = 1
            if self.current_road_index > 7:
                self.current_road_index = 7

            # 새로운 이미지 로드
            self.images = []
            for j in range(1, 5):
                image_path = resource_path(f'res/roads/road{self.current_road_index}_{j}.png')  # 경로 수정
                self.images.append(load_image(image_path))

        # 도로 변화에 따라 자동차 이동
        self.roadMove = ((self.current_road_index - 4) * self.speed) * 0.005

        self.fuel -= self.speed * 0.001
        self.speed += self.dspeed * gfw.frame_time * 10
        self.x += self.dx * self.speed * gfw.frame_time + self.roadMove
        self.x = clamp(self.min_x, self.x, self.max_x)
        self.score += self.speed * 0.01

        if self.x <= self.min_x or self.x >= self.max_x:
            self.dspeed = -2
            self.fuel *= 0.99
        elif self.speed < 0:
            self.speed = 0
            self.dspeed = 0
        elif self.dspeed == -1:
            self.dspeed = -1
        elif self.dspeed == -2:
            self.dspeed = 0

        if self.fuel <= 0:
            self.fuel = 0
            self.dspeed = -3
        if self.score % 500 == 1:
            self.fuel += 100

        self.x = self.x % self.width
        self.update_roll()

        if self.speed == 0:
            self.image_change_speed = 0
        else:
            self.image_change_speed = max(1, int(200 / (self.speed + 1)))

        self.frame_count += 1
        if self.image_change_speed > 0 and self.frame_count % self.image_change_speed == 0:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)

    def draw(self):
        current_image = self.images[self.current_image_index]
        current_image.draw(self.x, self.y)
        current_image.draw(self.x - self.width, self.y)

    def update_roll(self):
        roll_dir = self.dx
        if roll_dir == 0:
            if self.roll_time > 0:
                roll_dir = -1
            elif self.roll_time < 0:
                roll_dir = 1

        self.roll_time += roll_dir * gfw.frame_time
        self.roll_time = clamp(-Background.MAX_ROLL, self.roll_time, Background.MAX_ROLL)
        if self.dx == 0:
            if roll_dir < 0 and self.roll_time < 0:
                self.roll_time = 0
            if roll_dir > 0 and self.roll_time > 0:
                self.roll_time = 0
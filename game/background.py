# background.py

from pico2d import *
import random
import gfw

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
        super().__init__('res/roads/road1_1.png', get_canvas_width() // 2, get_canvas_height() // 2)
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

        self.engine = gfw.sound.sfx("res/sound/engine.wav")

        # 이미지 시리즈 로드
        self.images = []
        for j in range(1, 5):  # j는 1부터 4까지
            image_path = f'res/roads/road4_{j}.png'  # 기본적으로 road4의 이미지를 로드
            self.images.append(load_image(image_path))

        # 현재 도로 인덱스 초기화
        self.current_road_index = 4  # 초기 도로는 4로 설정
        self.current_image_index = 0
        self.image_change_speed = 1
        self.frame_count = 0

    def get_center_x(self):
        return self.x

    def handle_event(self, e):
        pair = (e.type, e.key)

        if pair in Background.KEY_MAP:
            self.dx += Background.KEY_MAP[pair]  # 키 입력에 따른 dx 값 조정
        elif pair in Background.SPEED_KEY_MAP and self.fuel>0:
            self.dspeed = Background.SPEED_KEY_MAP[pair]  # 키 입력에 따른 속도 변화 조정

            # 엔진 소리 재생 및 정지
            if e.type == SDL_KEYDOWN and e.key == SDLK_a:
                self.engine.play()

        # 디버깅용
        if e.key == SDLK_9:
            self.score = 10000
        if e.key == SDLK_0:
            self.fuel = 0

    def update(self):
        # 도로 변경 체크
        if self.roadCheck < self.score:
            # 일정 거리 도달 시 연료 제공
            if self.roadCheck%1000==0 and self.score!=0:
                self.fuel += 50
                if self.fuel > 1000:
                    self.fuel = 1000

            self.roadCheck += 50
            self.current_road_index += random.randint(-1,1)  # 도로 인덱스를 증가

            if self.current_road_index < 1:  # 최소 도로 인덱스가 0일 경우
                self.current_road_index = 1  # 0 이하는 허용하지 않음
            if self.current_road_index > 7:  # 최대 도로 인덱스가 7일 경우
                self.current_road_index = 7  # 7 이상은 허용하지 않음


            # 새로운 이미지 로드
            self.images = []
            for j in range(1, 5):
                image_path = f'res/roads/road{self.current_road_index}_{j}.png'
                self.images.append(load_image(image_path))

        #도로 변화에 따라 자동차 이동
        self.roadMove = ((self.current_road_index-4)*self.speed)*0.005

        self.fuel -= self.speed*0.001 #연료 감소
        self.speed += self.dspeed * gfw.frame_time * 10  # 속도 계산
        self.x += self.dx * self.speed * gfw.frame_time + self.roadMove  # x 위치 계산
        self.x = clamp(self.min_x, self.x, self.max_x)  # x 위치를 최소와 최대 값으로 제한
        self.score += self.speed*0.01#간 거리

        if self.x <= self.min_x or self.x >= self.max_x:
            self.dspeed = -2  # 최소 또는 최대 위치에 도달하면 속도 감소
            self.fuel *= 0.99
        elif self.speed < 0:
            self.speed = 0  # 속도가 음수가 되지 않도록 조정
            self.dspeed = 0
        elif self.dspeed == -1:
            self.dspeed = -1  # 속도 감소
        elif self.dspeed == -2:
            self.dspeed = 0  # 속도 변화 없음

        if self.fuel <= 0:
            self.fuel=0
            self.dspeed = -3
        if self.score % 500 == 1:
            self.fuel += 100



        self.x = self.x % self.width  # 배경이 반복되도록 설정
        self.update_roll()  # 롤링 업데이트

        # 이미지 변경 속도 조절
        if self.speed == 0:
            self.image_change_speed = 0
        else:
            self.image_change_speed = max(1, int(200 / (self.speed + 1)))

        self.frame_count += 1
        if self.image_change_speed > 0 and self.frame_count % self.image_change_speed == 0:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)  # 이미지 인덱스 업데이트

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

        self.roll_time += roll_dir * gfw.frame_time  # 롤링 시간 업데이트
        self.roll_time = clamp(-Background.MAX_ROLL, self.roll_time, Background.MAX_ROLL)  # 롤링 시간 제한
        if self.dx == 0:
            if roll_dir < 0 and self.roll_time < 0:
                self.roll_time = 0
            if roll_dir > 0 and self.roll_time > 0:
                self.roll_time = 0

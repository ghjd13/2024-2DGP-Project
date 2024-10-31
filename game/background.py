from pico2d import *
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
        (SDL_KEYDOWN, SDLK_a): 1,  # 속력
        (SDL_KEYUP, SDLK_a): 0,  # 속력
    }
    MAX_ROLL = 0.4  # 최대 롤 값

    def __init__(self):
        super().__init__('res/road1.png', get_canvas_width() // 2, get_canvas_height() // 2)
        self.dx = 0
        self.speed = 0  # 초당 320 픽셀 이동
        self.dspeed = 0
        self.width = self.image.w * Background.IMAGE_MAG
        self.height = self.image.h * Background.IMAGE_MAG
        self.min_x = 0
        self.max_x = get_canvas_width()
        self.roll_time = 0

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Background.KEY_MAP:
            self.dx += Background.KEY_MAP[pair]
        elif pair in Background.SPEED_KEY_MAP:
            self.dspeed = Background.SPEED_KEY_MAP[pair]
        print(self.speed, self.dspeed)

    def update(self):
        self.speed += self.dspeed * gfw.frame_time *10
        self.x += self.dx * self.speed * gfw.frame_time
        self.x = self.x % self.width  # 배경이 반복되도록 설정
        self.update_roll()

    def draw(self):
        self.image.draw(self.x, self.y)
        # 배경이 반복되도록 두 번째 이미지를 그리기
        self.image.draw(self.x - self.width, self.y)

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

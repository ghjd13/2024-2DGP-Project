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
        (SDL_KEYDOWN, SDLK_a): 1,  # 속력 증가
        (SDL_KEYUP, SDLK_a): 0,  # 속력 유지
        (SDL_KEYDOWN, SDLK_s): -1,  # 속력 감소
        (SDL_KEYUP, SDLK_s): 0,  # 속력 유지
    }
    MAX_ROLL = 0.4  # 최대 롤 값

    def __init__(self):
        super().__init__('res/road1.png', get_canvas_width() // 2, get_canvas_height() // 2)
        self.dx = 0  # x축 이동 거리
        self.speed = 0  # 현재 속도
        self.dspeed = 0  # 속도 변화
        self.width = self.image.w * Background.IMAGE_MAG  # 배경 이미지의 너비
        self.height = self.image.h * Background.IMAGE_MAG  # 배경 이미지의 높이
        self.min_x = get_canvas_width() // 4  # 최소 x 위치
        self.max_x = (get_canvas_width() // 4) * 3  # 최대 x 위치
        self.roll_time = 0  # 롤링 시간 초기화

        # 이미지 시리즈 로드
        self.images = [load_image(f'res/road{i}.png') for i in range(1, 5)]
        self.current_image_index = 0  # 현재 이미지 인덱스 초기화
        self.image_change_speed = 1  # 이미지 변경 속도
        self.frame_count = 0  # 프레임 카운트 초기화

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Background.KEY_MAP:
            self.dx += Background.KEY_MAP[pair]  # 키 입력에 따른 dx 값 조정
        elif pair in Background.SPEED_KEY_MAP:
            self.dspeed = Background.SPEED_KEY_MAP[pair]  # 키 입력에 따른 속도 변화 조정
        print(self.speed, self.dspeed)

    def update(self):
        if self.x <= self.min_x or self.x >= self.max_x:
            self.dspeed = -2  # 최소 또는 최대 위치에 도달하면 속도 감소
        elif self.speed < 0:
            self.speed = 0  # 속도가 음수가 되지 않도록 조정
            self.dspeed = 0
        elif self.dspeed == -1:
            self.dspeed = -1  # 속도 감소
        elif self.dspeed == -2:
            self.dspeed = 0  # 속도 변화 없음
        self.speed += self.dspeed * gfw.frame_time * 10  # 속도 계산
        self.x += self.dx * self.speed * gfw.frame_time  # x 위치 계산
        self.x = clamp(self.min_x, self.x, self.max_x)  # x 위치를 최소와 최대 값으로 제한

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
        current_image.draw(self.x, self.y)  # 현재 이미지를 그리기
        # 배경이 반복되도록 두 번째 이미지를 그리기
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

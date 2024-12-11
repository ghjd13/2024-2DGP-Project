from pico2d import *
import gfw


class Fighter(gfw.Sprite):
    IMAGE_MAG = 2 #이미지 확대율
    # 키 맵핑: 키 입력과 이동 방향을 매핑
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): -1,
        (SDL_KEYDOWN, SDLK_RIGHT): 1,
        (SDL_KEYUP, SDLK_LEFT): 1,
        (SDL_KEYUP, SDLK_RIGHT): -1,
    }
    MAX_ROLL = 0.4  # 최대 롤 값
    IMAGE_RECTS = [
        (0, 0, 45, 26),
        (46, 0, 39, 26),
        (86, 0, 37, 26),
        (125, 0, 38, 26),
        (165, 0, 39, 26),
        (206, 0, 38, 26),
        (246, 0, 38, 26),
        (285, 0, 40, 26),
        (326, 0, 45, 26),
    ]
    IMAGE_MAGNIFICATION_RECTS = [
        (45*IMAGE_MAG, 26*IMAGE_MAG),
        (39*IMAGE_MAG, 26*IMAGE_MAG),
        (37*IMAGE_MAG, 26*IMAGE_MAG),
        (38*IMAGE_MAG, 26*IMAGE_MAG),
        (39*IMAGE_MAG, 26*IMAGE_MAG),
        (38*IMAGE_MAG, 26*IMAGE_MAG),
        (38*IMAGE_MAG, 26*IMAGE_MAG),
        (40*IMAGE_MAG, 26*IMAGE_MAG),
        (45*IMAGE_MAG, 26*IMAGE_MAG),
    ]

    def __init__(self):
        # Fighter 클래스 초기화
        super().__init__('res/cars.png', get_canvas_width() // 2, 80)
        self.dx = 0
        self.speed = 320  # 초당 320 픽셀 이동
        self.width = 72
        half_width = self.width // 2
        self.min_x = half_width
        self.max_x = get_canvas_width() - half_width
        self.laser_time = 0
        self.roll_time = 0
        self.src_rect = Fighter.IMAGE_RECTS[4]  # 0~8의 9개 중 4번이 가운데
        self.src_mag_rect = Fighter.IMAGE_MAGNIFICATION_RECTS[4]

    def handle_event(self, e):
        # 이벤트 처리
        pair = (e.type, e.key)
        if pair in Fighter.KEY_MAP:
            self.dx += Fighter.KEY_MAP[pair]

    def update(self):
        # 매 프레임마다 업데이트
        self.update_roll()

    def update_roll(self):
        # 비행기의 롤 업데이트
        roll_dir = self.dx
        if roll_dir == 0:  # 현재 비행기가 움직이지 않을 때
            if self.roll_time > 0:  # roll이 + 라면
                roll_dir = -1  # 감소시킴
            elif self.roll_time < 0:  # roll이 - 라면
                roll_dir = 1  # 증가시킴

        self.roll_time += roll_dir * gfw.frame_time
        self.roll_time = clamp(-Fighter.MAX_ROLL, self.roll_time, Fighter.MAX_ROLL)
        if self.dx == 0:  # 현재 비행기가 움직이지 않을 때
            if roll_dir < 0 and self.roll_time < 0:  # roll이 감소 중이었고 0을 지나쳤을 때
                self.roll_time = 0  # 0으로 설정
            if roll_dir > 0 and self.roll_time > 0:  # roll이 증가 중이었고 0을 지나쳤을 때
                self.roll_time = 0  # 0으로 설정

        roll = int(self.roll_time * 4 / Fighter.MAX_ROLL)
        self.src_rect = Fighter.IMAGE_RECTS[roll + 4]  # [-4 ~ +4]를 [0 ~ 8]로 변환
        self.src_mag_rect = Fighter.IMAGE_MAGNIFICATION_RECTS[roll + 4]
    def draw(self):
        # 화면에 그리기
        self.image.clip_draw(*self.src_rect, self.x, self.y, self.src_mag_rect[0], self.src_mag_rect[1])
        # if self.laser_time < Fighter.SPARK_INTERVAL:
        #     self.spark_image.draw(self.x, self.y + Fighter.SPARK_OFFSET)

    def get_bb(self):
        # 충돌 박스 반환
        return self.x - 42, self.y - 26, self.x + 42, self.y + 26

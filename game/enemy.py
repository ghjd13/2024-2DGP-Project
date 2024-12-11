# enemy.py

from pico2d import *
import random
import gfw


class Enemy(gfw.AnimSprite):
    IMAGE_RECTS = [
        # 적 스프라이트의 다양한 애니메이션 프레임
        ((0, 0, 45, 24),
         (46, 0, 40, 24),
         (86, 0, 38, 24),
         (127, 0, 37, 24),
         (166, 0, 39, 24),
         (206, 0, 37, 24),
         (246, 0, 38, 24),
         (285, 0, 40, 24),
         (326, 0, 45, 24),),
    ]
    WIDTH = 100
    MIN_SCALE = 0.2  # 최소 스케일
    MAX_SCALE = 2.5  # 최대 스케일
    gauge = None

    def __init__(self, enemy_x, background):
        self.background = background  # 배경 객체 저장
        self.x = enemy_x  # 생성된 x 좌표로 설정
        self.y = get_canvas_height() // 2  # y 위치를 화면 중간으로 설정
        super().__init__(f'res/police_Car.png', self.x, self.y, 10)  # 10fps 속도로 적 스프라이트 로드

        self.speed = -100  # 이동 속도 (초당 100 픽셀)
        self.max_life = 100  # 최대 생명력 설정 (고정값)
        self.life = self.max_life  # 현재 생명력은 최대 생명력으로 시작
        self.score = self.max_life  # 점수는 최대 생명력과 동일

        # 게이지 로드
        if Enemy.gauge is None:
            Enemy.gauge = gfw.Gauge('res/gauge_fg.png', 'res/gauge_bg.png')
            print('게이지를 한 번만 로드합니다')

        self.layer_index = gfw.top().world.layer.enemy  # 렌더링을 위한 레이어 인덱스
        self.frame_index = 0  # 현재 프레임 인덱스

    def update(self):
        # 적의 위치 업데이트
        self.y += self.speed * gfw.frame_time
        self.x += self.background.dx * self.background.speed * gfw.frame_time

        if self.y < -self.WIDTH:
            gfw.top().world.remove(self)  # 화면 밖으로 나가면 적 제거

        self.frame_index = (self.frame_index + 1) % len(self.IMAGE_RECTS[0])  # 프레임 인덱스 업데이트

    def draw(self):
        # 적 스프라이트 그리기
        frame = self.IMAGE_RECTS[0][self.background.current_road_index]  # 현재 프레임 선택

        # 적이 아래로 갈수록 크기를 키움 (0.2배에서 2.5배)
        canvas_height = get_canvas_height()
        scale = max(Enemy.MIN_SCALE,
                    min(Enemy.MAX_SCALE, 0.2 + (canvas_height - self.y) / canvas_height * (Enemy.MAX_SCALE - 0.2)))

        self.image.clip_draw(*frame, self.x, self.y, frame[2] * scale, frame[3] * scale)  # 스케일을 적용하여 이미지 그리기
        gy = self.y - self.WIDTH // 2  # 게이지 위치 계산
        rate = self.life / self.max_life  # 남은 생명력 비율 계산
        self.gauge.draw(self.x, gy, self.WIDTH - 10, rate)  # 생명력 게이지 그리기

    def get_bb(self):
        # 현재 프레임의 크기를 바탕으로 바운딩 박스 설정
        frame = self.IMAGE_RECTS[0][self.frame_index]
        canvas_height = get_canvas_height()
        scale = max(Enemy.MIN_SCALE,
                    min(Enemy.MAX_SCALE, 0.2 + (canvas_height - self.y) / canvas_height * (Enemy.MAX_SCALE - 0.2)))
        left = self.x - (frame[2] * scale) // 2
        bottom = self.y - (frame[3] * scale) // 2
        right = self.x + (frame[2] * scale) // 2
        top = self.y + (frame[3] * scale) // 2
        return left, bottom, right, top



class EnemyGen:
    GEN_INTERVAL = 5.0  # 적 생성 간격 시간
    GEN_INIT = 1.0  # 초기 생성 지연 시간

    def __init__(self, background):
        self.time = self.GEN_INTERVAL - self.GEN_INIT  # 타이머 초기화
        self.wave_index = 0  # 파도 인덱스 초기화
        self.background = background  # 배경 객체 저장

    def draw(self): pass

    def update(self):
        self.time += gfw.frame_time  # 타이머 업데이트
        if self.time < self.GEN_INTERVAL:
            return  # 생성 간격 시간이 지나지 않았으면 대기

        # 도로 인덱스에 따라 x 좌표 범위를 가져오기
        min_x, max_x = self.get_x_range(self.background.current_road_index)
        enemy_x = random.randint(min_x, max_x)  # 배경의 중심을 기준으로 랜덤 x 좌표 설정

        enemy = Enemy(enemy_x, self.background)  # 생성된 x 좌표로 적 생성
        gfw.top().world.append(enemy, gfw.top().world.layer.enemy)

        self.time -= self.GEN_INTERVAL  # 타이머 초기화

    def get_x_range(self, road_index):
        # 도로 인덱스에 따라 x값 범위를 변경
        if road_index == 1:
            return (-30, 90)
        elif road_index == 2:
            return (140, 260)
        elif road_index == 3:
            return (180, 300)
        elif road_index == 4:
            return (260, 380)
        elif road_index == 5:
            return (320, 460)
        elif road_index == 6:
            return (360, 480)
        elif road_index == 7:
            return (480, 600)
        else:
            return (0, 640)  # 기본 범위
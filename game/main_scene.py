# main_scene.py

from pico2d import *
from gfw import *

from background import Background
from fighter import Fighter
from enemy import EnemyGen

# 게임 월드를 생성하고 레이어를 설정합니다.
world = gfw.World(['background', 'fighter', 'bullet', 'enemy', 'ui', 'controller'])

# 캔버스의 너비와 높이를 설정합니다.
canvas_width = 640
canvas_height = 480
# 경계 상자와 객체 수를 표시할지 여부를 설정합니다.
shows_bounding_box = True
shows_object_count = True


def enter():
    global sky, screen_move,desert, background, fighter, score_sprite, fuel_sprite, speed_sprite

    # 배경 객체를 먼저 초기화합니다.
    background = Background()

    # 배경 이미지를 추가합니다.
    desert = gfw.Background("res/desert.png")

    screen_move = (background.dx * background.speed) * 10
    sky = gfw.HorzFillBackground("res/NightSky.png", screen_move)


    world.append(sky, world.layer.background)
    world.append(desert, world.layer.background)
    world.append(background, world.layer.background)


    # 전투기 객체를 생성하고 추가합니다.
    fighter = Fighter()
    world.append(fighter, world.layer.fighter)

    # UI 레이어에 점수 스프라이트를 추가합니다.
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width - 50, canvas_height - 50)
    world.append(score_sprite, world.layer.ui)

    # UI 레이어에 연료 스프라이트를 추가합니다.
    fuel_sprite = gfw.ScoreSprite('res/number_24x32.png', 75, 50)
    world.append(fuel_sprite, world.layer.ui)

    # UI 레이어에 속도 스프라이트를 추가합니다.
    speed_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width - 50, 50)
    world.append(speed_sprite, world.layer.ui)

    # 적 생성기와 충돌 검사기를 추가합니다.
    world.append(EnemyGen(background), world.layer.controller)
    world.append(CollisionChecker(), world.layer.controller)

    # 점수, 연료, 속도를 초기화합니다.
    global score
    score = 0
    global fuel
    fuel = 100
    global speed
    speed = 100

def exit():
    # 월드를 정리합니다.
    world.clear()
    print('[main.exit()]')


def pause():
    print('[main.pause()]')


def resume():
    print('[main.resume()]')


def handle_event(e):
    # 특정 키가 눌렸을 때 월드 객체를 출력합니다.

    background.handle_event(e)
    # 전투기 객체에 이벤트를 전달합니다.
    fighter.handle_event(e)


class CollisionChecker:
    def draw(self):
        pass

    def update(self):
        screen_move = (background.dx * background.speed) * 10

        # 적 객체를 가져옵니다.
        enemies = world.objects_at(world.layer.enemy)

        self.score = background.score
        score_sprite.score = self.score // 100

        self.fuel = background.fuel
        fuel_sprite.score = self.fuel // 1

        self.speed = background.speed
        speed_sprite.score = self.speed // 1

        for e in enemies:
            collided = False
            if collided: break
            # 자동차와 적이 충돌했는지 확인합니다.
            if gfw.collides_box(fighter, e):
                world.remove(e)
                break
        pass


class MainScenUI:
    def __init__(self):
        # 폰트를 로드하고 위치를 설정합니다.
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)

    def update(self): pass

    def draw(self):
        # 점수를 화면에 그립니다.
        self.font.draw(*self.pos, f'{score:10d}KM')


if __name__ == '__main__':
    # 메인 모듈을 시작합니다.
    gfw.start_main_module()

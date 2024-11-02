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
    # 배경 이미지를 추가합니다.
    # bg = InfiniteScrollBackground('res/road1.png', margin=100)
    # world.append(bg, world.layer.bg)
    # world.bg = bg
    global background
    background = Background()
    world.append(background, world.layer.background)

    # 전투기 객체를 생성하고 추가합니다.
    global fighter
    fighter = Fighter()
    world.append(fighter, world.layer.fighter)

    # UI 레이어에 점수 스프라이트를 추가합니다.
    global score_sprite
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width - 50, canvas_height - 50)
    world.append(score_sprite, world.layer.ui)

    # 적 생성기와 충돌 검사기를 추가합니다.
    # world.append(EnemyGen(), world.layer.controller)
    # world.append(CollisionChecker(), world.layer.controller)

    # 점수를 초기화합니다.
    global score
    score = 0


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
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_1:
            print(world.objects)

    background.handle_event(e)
    # 전투기 객체에 이벤트를 전달합니다.
    fighter.handle_event(e)


class CollisionChecker:
    def draw(self):
        pass

    def update(self):
        # # 적 객체를 가져옵니다.
        # enemies = world.objects_at(world.layer.enemy)
        # for e in enemies:  # 역순으로 순회합니다.
        #     collided = False
        #     # 총알 객체를 가져옵니다.
        #     bullets = world.objects_at(world.layer.bullet)
        #     for b in bullets:  # 역순으로 순회합니다.
        #         # 총알과 적이 충돌했는지 확인합니다.
        #         if gfw.collides_box(b, e):
        #             collided = True
        #             world.remove(b)
        #             # 적의 생명력을 감소시킵니다.
        #             dead = e.decrease_life(b.power)
        #             if dead:
        #                 global score
        #                 score += e.score
        #                 score_sprite.score = score
        #                 # print(f'+{e.score} ={score}')
        #                 world.remove(e)
        #             break
        #     if collided: break
        #     # 전투기와 적이 충돌했는지 확인합니다.
        #     if gfw.collides_box(fighter, e):
        #         world.remove(e)
        #         # 전투기의 HP를 감소시킵니다.
        #         break
        pass


class MainScenUI:
    def __init__(self):
        # 폰트를 로드하고 위치를 설정합니다.
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)

    def update(self): pass

    def draw(self):
        # 점수를 화면에 그립니다.
        self.font.draw(*self.pos, f'{score:10d}')


if __name__ == '__main__':
    # 메인 모듈을 시작합니다.
    gfw.start_main_module()

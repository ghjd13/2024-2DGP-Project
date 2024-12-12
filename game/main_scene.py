# main_scene.py

from pico2d import *
from gfw import *

from background import Background
from fighter import Fighter
from enemy import EnemyGen
import highscore

# 게임 월드를 생성하고 레이어를 설정합니다.
world = gfw.World(['background', 'fighter', 'bullet', 'enemy', 'ui', 'controller', 'over'])

# 캔버스의 너비와 높이를 설정합니다.
canvas_width = 640
canvas_height = 480
# 경계 상자와 객체 수를 표시할지 여부를 설정합니다.
shows_bounding_box = True
shows_object_count = True


def enter():
    global sky, city, desert, background, fighter, score_sprite, fuel_sprite, speed_sprite,UI

    # 배경 객체를 먼저 초기화합니다.
    background = Background()

    # 배경 이미지를 추가합니다.
    desert = gfw.Background("res/desert.png")

    city = gfw.HorzFillBackground('res/city.png')

    sky = gfw.HorzFillBackground("res/NightSky.png")

    UI = gfw.Background("res/UI.png")


    world.append(sky, world.layer.background)
    world.append(city, world.layer.background)
    world.append(desert, world.layer.background)
    world.append(background, world.layer.background)

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

    world.append(UI, world.layer.background)

    # 적 생성기와 충돌 검사기를 추가합니다.
    world.append(EnemyGen(background), world.layer.controller)
    world.append(CollisionChecker(), world.layer.controller)

    # 점수, 연료, 속도를 초기화합니다.
    global score
    score = 0
    global fuel
    fuel = 1000
    global speed
    speed = 1000

    global crash, mainMusic
    crash = gfw.sound.sfx("res/sound/crash.wav")
    mainMusic = gfw.sound.music("res/sound/mainMusic.mp3")

    mainMusic.play()
    mainMusic.repeat_play()

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

def is_game_over():
    return background.fuel<=0 and background.speed<=0

def is_ending():
    return background.score>=10000

def end_game(ending):
    highscore.add(background.score, ending)
    gfw.push(highscore)



class CollisionChecker:
    def draw(self):
        pass

    def update(self):

        # 적 객체를 가져옵니다.
        enemies = world.objects_at(world.layer.enemy)

        if is_game_over():
            end_game(0)
        if is_ending():
            end_game(1)

        sky.speed = (background.dx * background.speed) * 0.1
        city.speed = (background.dx * background.speed) * 0.5
        city.y = (canvas_height*((background.score/100)*0.01))-400

        self.score = background.score
        score_sprite.score = self.score // 10

        self.fuel = background.fuel
        fuel_sprite.score = self.fuel // 10

        self.speed = background.speed
        speed_sprite.score = self.speed //1

        for e in enemies:
            # 자동차와 적이 충돌했는지 확인합니다.
            if gfw.collides_box(fighter, e) and not e.collided:
                crash.play()
                background.speed *= 0.9  # 속도 감속
                background.fuel *= 0.99
                e.basicSpeed = e.basicSpeed * 1.001  # 넉백
                e.collided = True
                break
            else:
                e.collided = False

        pass



class MainScenUI:
    def __init__(self):
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        self.font.draw(*self.pos, f'{score:10d}')


if __name__ == '__main__':
    # 메인 모듈을 시작합니다.
    gfw.start_main_module()

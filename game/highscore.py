from pico2d import *
from gfw import *
import pickle

FILENAME = 'score.pickle'

canvas_width = 640
canvas_height = 480

transparent = True

world = World(2)

import sys
self = sys.modules[__name__]

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.localtime()
    def timestr(self):
        return time.strftime('%Y-%m-%d %H:%M', self.time)


try:
    f = open(FILENAME, "rb")
    scores = pickle.load(f)
    f.close()
    print("Scores:", scores)
except:
    print("No highscore file")
    scores = [ ]

just_added = None
def add(score, ending):
    entry = Entry(score)
    global just_added
    just_added = entry

    global Ending
    Ending =ending

    global scores
    scores.append(entry)
    scores.sort(key=lambda e:e.score)
    scores = scores[:10]
    try:
        with open(FILENAME, "wb") as f:
            pickle.dump(scores, f)
    except:
        pass

def enter():
    global game_over_sprite, good_ending_sprite
    game_over_sprite = gfw.Background('res/game_over.png')
    good_ending_sprite = gfw.Background('res/good_ending.png')

    if Ending == 0:
        world.append(game_over_sprite, 1)
    elif Ending == 1:
        world.append(good_ending_sprite, 1)

    global frame_9p
    frame_9p = gfw.image.NinePatch(gfw.image.load('res/hs_frame.png'), 30, 30, 30, 30)

    global font
    font = gfw.font.load('res/PF스타더스트.TTF', 25)
    world.append(self, 1)

def exit():
    world.clear()

def update():
    pass

COLOR_NORMAL = (0, 0, 0)
COLOR_ADDED = (0, 0, 192)
def draw():
    cw, ch = get_canvas_width(), get_canvas_height()
    frame_9p.draw(cw // 2, ch // 2, cw - 100, ch - 100)
    x, y = 150, ch - 112
    for score in scores:
        color = COLOR_ADDED if score == just_added else COLOR_NORMAL
        font.draw(x, y, f'{score.score:5.1f}KM', color)
        gfw.font.draw_centered_text(font, "",x, y, color)
        font.draw(x + 150, y, score.timestr(), color)
        y -= 35

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
        return

    if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
        global just_added
        gfw.pop()
        if just_added is not None:
            gfw.pop()
        just_added = None
        return True

if __name__ == '__main__':
    gfw.start_main_module()


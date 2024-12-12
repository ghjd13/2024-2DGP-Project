from gfw import *
from pico2d import *
import main_scene

import sys
self = sys.modules[__name__]

canvas_width = main_scene.canvas_width
canvas_height = main_scene.canvas_height

world = World(2)

def enter():
    world.append(HorzFillBackground('res/UI/menuScreen.png'), 0)
    world.append(Sprite('res/UI/GameStartButton.png', 100, 200), 0)
    world.append(Sprite('res/UI/GameDescriptionButton.png', 100, 75), 0)

    import json

def exit():
    pass

    # gfw.font.unload(font)

def update():
    pass

def draw():
    pass

def handle_event(e):
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_UP:
            pass
        if e.key == SDLK_DOWN:
            pass
        if e.key == SDLK_RETURN:
            gfw.push(main_scene)

def pause(): pass
def resume(): pass

if __name__ == '__main__':
    gfw.start_main_module()


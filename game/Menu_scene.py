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
    startButton = Sprite('res/UI/GameStartButton.png', 100, 200)
    world.append(startButton, 0)
    descriptionButton = Sprite('res/UI/GameDescriptionButton.png', 100, 75)
    world.append(descriptionButton, 0)

    import json

def exit():
    pass

    # gfw.font.unload(font)

def update():
    pass

def draw():
    pass

def handle_event(e):
    if e.type == SDL_MOUSEBUTTONDOWN:
        mx, my = e.x, e.y
        if mx > 37 and mx < 163 and my > 217 and my <343:
            gfw.push(main_scene)
        elif mx > 37 and mx < 163 and my > 343 and my <468:
            gfw.push(main_scene)
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            gfw.push(main_scene)

def pause(): pass
def resume(): pass

if __name__ == '__main__':
    gfw.start_main_module()


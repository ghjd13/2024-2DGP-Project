from gfw import *
from pico2d import *
import main_scene

import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

self = sys.modules[__name__]

canvas_width = main_scene.canvas_width
canvas_height = main_scene.canvas_height

world = World(2)

class ChangeObject:
    def __init__(self, image):
        self.image = load_image(image)

    def update(self):
        pass

    def draw(self):
        self.image.draw(canvas_width // 2, canvas_height // 2)

def enter():
    global change, Description, Title, startButton, descriptionButton, bg
    bg = HorzFillBackground(resource_path('res/menu/menuScreen.png'))
    world.append(bg, 0)
    Description = ChangeObject(resource_path('res/menu/Description.png'))
    Title = ChangeObject(resource_path('res/menu/Title.png'))
    change = Title

    startButton = Sprite(resource_path('res/menu/GameStartButton.png'), 100, 200)
    world.append(startButton, 0)
    descriptionButton = Sprite(resource_path('res/menu/GameDescriptionButton.png'), 100, 75)
    world.append(descriptionButton, 0)
    world.append(change, 0)

    menuMusic = gfw.sound.music(resource_path("res/sound/Menu.mp3"))
    menuMusic.play()
    menuMusic.repeat_play()

def exit():
    pass

def update():
    pass

def draw():
    pass

def handle_event(e):
    global change, startButton, descriptionButton, bg
    if e.type == SDL_MOUSEBUTTONDOWN:
        mx, my = e.x, e.y
        if change == Title:
            if mx > 37 and mx < 163 and my > 217 and my < 343:
                gfw.push(main_scene)
            elif mx > 37 and mx < 163 and my > 343 and my < 468:
                change = Description
        else:
            pass

    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            gfw.push(main_scene)
        elif e.key == SDLK_q and change == Description:
            change = Title

    objects = list(world.objects[0])
    last_object = objects.pop()
    world.objects[0] = objects
    world.append(change, 0)

def pause(): pass
def resume(): pass

if __name__ == '__main__':
    gfw.start_main_module()
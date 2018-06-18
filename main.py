import sys
import time
import pygame

from frame.frame import Frame
from frame.world import World
from frame.image_library import ImageLibrary
from objects.game_object.dinamic.characters.kirito import Kirito
from objects.game_object.static.background import Background
from input.key_log.key_logger import KeyLogger
from input.key_log.mouse import Mouse
from main_game.game_states import GameStates
from objects.images.animation_library import AnimationLibrary
from physics.coordinates import Coordinates
from frame.settings import Settings
from objects.game_object.dinamic.obstacles.blocks.grey_block import GreyBlock
from objects.game_object.dinamic.obstacles.targets.classic_target import ClassicTarget
from frame.borders import Borders
from main_game.level import Level
from objects.widgets.buttons.save_button import SaveButton


Settings()
ImageLibrary()
frame = Frame()
AnimationLibrary(frame)
Borders()
World()
KeyLogger()
Mouse()


Borders.lock()
game_states = GameStates()
game_states.change_submenu(4)
game_states.state = GameStates.MENU


if __name__ == '__main__':
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.write_settings()
                running = False
            elif event.type == pygame.KEYDOWN:
                KeyLogger.key_press(event.key, event.mod)
            elif event.type == pygame.KEYUP:
                KeyLogger.key_release(event.key, event.mod)
            elif event.type == pygame.MOUSEMOTION:
                Mouse.reposition(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse.button_press(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                Mouse.button_release(event.button)
            elif event.type == pygame.VIDEORESIZE:
                frame.resize(event.w, event.h)
                Settings.write_settings()

        time.sleep(1/60)

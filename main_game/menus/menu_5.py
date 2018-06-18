import pygame

import thread_lock
from frame.borders import Borders
from frame.frame import Frame
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.level import Level
from main_game.menu import Menu
from objects.game_object.dinamic.spawn import Spawn
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.buttons.save_button import SaveButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Bounds(object):
    pass


class Menu_5(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 5, 4)
        self.add_list([MenuTextButton('Build', 30, Coordinates(10, 15), Coordinates(325, 50), self.click_build,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Level Select', 30, Coordinates(10, 15), Coordinates(325, 110), self.click_lselect,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Main Menu', 30, Coordinates(10, 15), Coordinates(325, 170), self.click_main_menu,
                                      scale=Coordinates(1.5, 1)),
                       Background('resources\\test_images\\white_background.png')])

    def click_build(self):
        self.empty()
        bck = Background('resources\\test_images\\white_background.png')
        World.add(bck)
        save_button = SaveButton()
        save_button.coordinates = Coordinates(650, 500)
        World.add(save_button)
        level = Level(self.gamestates, '')
        World.setup_level(level)
        thread_lock.pause_main = False
        self.gamestates.state = self.gamestates.BUILDER
        Frame.default_coordinates = Coordinates(0, 0)
        if Borders.focus_object is None:
                Borders.gain_focus(World.main_character)
        Borders.lock()
        pygame.event.set_grab(Settings.mouse_confined)
        self.gamestates.sleep()

    def click_lselect(self):
        self.change_to(6)

    def click_main_menu(self):
        self.back()

import pygame

from frame.borders import Borders
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_13(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 13, 11)
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(10, 10), self.click_back),
                       Background('resources\\test_images\\white_background.png')])
        self.mouse_confined_button = MenuTextButton('', 30, Coordinates(10, 15), Coordinates(300, 50),
                                                    self.confine, Coordinates(2, 1))

    def update(self):
        self.update_confined()

    def update_confined(self):
        World.remove(self.mouse_confined_button)
        if Settings.mouse_confined:
            self.mouse_confined_button.texts[0].set_text('Mouse confined')
        else:
            self.mouse_confined_button.texts[0].set_text('Mouse unconfined')
        World.add(self.mouse_confined_button)

    def confine(self):
        if Settings.mouse_confined:
            Settings.mouse_confined = False
            Settings.write_settings()
        else:
            Settings.mouse_confined = True
            Settings.write_settings()
        self.update_confined()

    def click_back(self):
        self.back()

    def begin(self):
        self.update()

    def end(self):
        World.remove(self.mouse_confined_button)

import pygame

from frame.borders import Borders
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.widgets.buttons.menu_text_button import MenuTextButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_9(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 9, 2)  # 2 - play mode
        self.add(self.change_perspective, 1 / 1)
        self.add(self.focus, 1 / target_fps)
        self.add_list([MenuTextButton('Resume', 30, Coordinates(10, 15), Coordinates(50, 50), self.click_resume,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Main Menu', 30, Coordinates(10, 15), Coordinates(50, 110), self.click_main_menu,
                                      scale=Coordinates(1.5, 1))])

    def click_resume(self):
        pygame.event.set_grab(Settings.mouse_confined)
        self.back()

    def click_main_menu(self):
        World.full_clear()
        self.change_to(4)

    def begin(self):
        Borders.lose_focus()
        Borders.unlock()

    def focus(self):
        Borders.focus()
        return True

    def change_perspective(self):
        if KeyLogger.bindings['perspective'].check():
            if Borders.focus_object is None:
                Borders.gain_focus(World.main_character)
                Borders.lock()
            else:
                Borders.lose_focus()
                Borders.unlock()
            return True
        return False

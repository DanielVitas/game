from frame.borders import Borders
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_4(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 4, 0)  # 0 - quit
        self.add_list([MenuTextButton('Play', 30, Coordinates(10, 15), Coordinates(325, 50), self.click_play,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Characters', 30, Coordinates(10, 15), Coordinates(325, 110),
                                      self.click_character_select, scale=Coordinates(1.5, 1)),
                       MenuTextButton('Settings', 30, Coordinates(10, 15), Coordinates(325, 170),
                                      self.click_settings, scale=Coordinates(1.5, 1)),
                       MenuTextButton('Credits', 30, Coordinates(10, 15), Coordinates(325, 230),
                                      self.click_credits, scale=Coordinates(1.5, 1)),
                       MenuTextButton('Quit', 30, Coordinates(10, 15), Coordinates(325, 290), self.click_quit,
                                      scale=Coordinates(1.5, 1)),
                       Background('resources\\test_images\\white_background.png')])

    def click_play(self):
        self.change_to(5)

    def click_character_select(self):
        self.change_to(8)

    def click_settings(self):
        self.change_to(11)

    def click_credits(self):
        self.change_to(14)

    def click_quit(self):
        self.back()

    def end(self):
        World.full_clear()

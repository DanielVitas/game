from frame.borders import Borders
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_11(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 11, 4)
        self.add_list([MenuTextButton('User Settings', 30, Coordinates(10, 15), Coordinates(325, 50), self.click_us,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Key Bindings', 30, Coordinates(10, 15), Coordinates(325, 110), self.click_keyb,
                                      scale=Coordinates(1.5, 1)),
                       MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(325, 170), self.click_back,
                                      scale=Coordinates(1.5, 1)),
                       Background('resources\\test_images\\white_background.png')])

    def click_us(self):
        self.change_to(13)

    def click_keyb(self):
        self.change_to(12)

    def click_back(self):
        self.back()

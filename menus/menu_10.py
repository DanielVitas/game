from frame.borders import Borders
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.label import Label
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_10(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 10, 6)
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(325, 500), self.click_back,
                                      scale=Coordinates(1.5, 1)),
                       Background('resources\\test_images\\green_background.png')])

    def click_back(self):
        self.back()

    def begin(self):
        World.full_clear()

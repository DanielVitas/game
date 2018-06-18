from frame.borders import Borders
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.text_holders.level_name import LevelName
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_14(Menu):
    credit_string = 'Game Creator:  Daniel Vitas'
    mentor = 'Mentor:  Matija Pretnar'
    adiitional_design = 'Additional design:  Žiga Avbreht, Uroš Šinigoj'
    beta_testers = 'Beta testers:  Rok Korpar, Matej Janežič'
    special_thx = 'Special thanks:  Aljosa Rebolj, Erazem Černe Pezdir, Nejc Hirci,'
    special_thx2 = 'Luka Miklavčič'

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 14, 4)
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(10, 10), self.click_back),
                       LevelName(Menu_14.credit_string, 40, Coordinates(100, 100)),
                       LevelName(Menu_14.mentor, 40, Coordinates(100, 150)),
                       LevelName(Menu_14.adiitional_design, 30, Coordinates(100, 300)),
                       LevelName(Menu_14.beta_testers, 30, Coordinates(100, 350)),
                       LevelName(Menu_14.special_thx, 30, Coordinates(100, 400)),
                       LevelName(Menu_14.special_thx2, 30, Coordinates(100, 430)),
                       Background('resources\\test_images\\white_background.png')])

    def click_back(self):
        self.back()

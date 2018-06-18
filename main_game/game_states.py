import time

import pygame

import threads.thread as thread
from frame.settings import Settings
from main_game.game_classic import GameClassic
from main_game.game_builder import GameBuilder
from main_game.menu_library import MenuLibrary
import thread_lock
from frame.world import World
from objects.game_object.dinamic.characters.kirito import Kirito
from objects.game_object.dinamic.characters.cat import Cat
from objects.game_object.dinamic.characters.marjan import Marjan
from objects.game_object.dinamic.characters.pretnar import Pretnar
from objects.game_object.dinamic.characters.martinator import Martinator
from objects.game_object.dinamic.characters.feguros import Feguros
from objects.game_object.dinamic.characters.batejgrid import Batejgrid
from objects.widgets.label import Label
from objects.widgets.text_holders.targets_left import TargetsLeft


class GameStates(object):
    state = None
    MENU = 0
    BUILDER = 1
    GAME = 2

    def __init__(self):
        self.state = self.GAME
        self.submenu = 4
        self.target_label = TargetsLeft()
        self.menu_library = MenuLibrary(self)
        self.game_classic = GameClassic(self)
        self.game_builder = GameBuilder(self)
        self.thread = thread.Thread(self.run, (), 'game states')
        self.sleep_time = 0
        self.sleep_start = 0

    def run(self):
        if time.time() - self.sleep_start > self.sleep_time:
            if self.state == self.GAME:
                self.game_classic.run()
                self.target_label.update(World.level.get_target_number())
            elif self.state == self.BUILDER:
                self.game_builder.run()
            elif self.state == self.MENU:
                self.menu_library.menus[self.submenu].run()

    def change_submenu(self, new_submenu):
        if self.state in [self.GAME, self.BUILDER]:
            thread_lock.pause_main = True
            World.pause()
            pygame.event.set_grab(False)
        else:
            self.menu_library.menus[self.submenu].end()
            self.menu_library.menus[self.submenu].empty()
        self.submenu = new_submenu
        self.menu_library.menus[self.submenu].begin()
        self.menu_library.menus[self.submenu].load()
        self.state = self.MENU
        self.sleep()

    def sleep(self, seconds=1 / 5):
        self.sleep_time = seconds
        self.sleep_start = time.time()

    def victory(self):
        self.change_submenu(10)

    @staticmethod
    def spawn(coordinates, main_character=None):
        if main_character is None:
            main_character = Settings.main_character_name
        mc = eval('%s()' % main_character)
        mc.coordinates = coordinates
        World.promote_main(mc)
        World.add(mc)

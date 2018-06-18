import os

import pygame

import thread_lock
from frame.borders import Borders
from frame.frame import Frame
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.level import Level
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.buttons.save_button import SaveButton
from objects.widgets.text_holders.level_name import LevelName
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_7(Menu):

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 7, 6)
        self.add_list([MenuTextButton('Play', 30, Coordinates(10, 15), Coordinates(500, 50), self.click_play),
                       MenuTextButton('Edit', 30, Coordinates(10, 15), Coordinates(500, 110), self.click_edit),
                       MenuTextButton('Rename', 30, Coordinates(10, 15), Coordinates(500, 170), self.click_rename),
                       MenuTextButton('Delete', 30, Coordinates(10, 15), Coordinates(500, 230), self.click_delete),
                       MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(500, 290), self.click_back),
                       Background('resources\\test_images\\white_background.png')])
        self.path = None
        self.name_label = None

    def display_name(self):
        name = self.path.split('\\')[-1][:-4]
        lname = LevelName(name, 50, Coordinates(100, 100))
        self.name_label = lname
        World.add(lname)

    def click_play(self):
        self.end()
        self.empty()
        bck = Background('resources\\test_images\\white_background.png')
        World.add(bck)
        level = Level(self.gamestates, self.path.split('\\')[-1][:-4])
        World.setup_level(level)
        World.add(self.gamestates.target_label)
        thread_lock.pause_main = False
        self.gamestates.state = self.gamestates.GAME
        Frame.default_coordinates = Coordinates(0, 0)
        if Borders.focus_object is None:
            Borders.gain_focus(World.main_character)
        Borders.lock()
        pygame.event.set_grab(Settings.mouse_confined)
        self.gamestates.sleep()

    def click_edit(self):
        self.end()
        self.empty()
        bck = Background('resources\\test_images\\white_background.png')
        World.add(bck)
        save_button = SaveButton()
        save_button.coordinates = Coordinates(650, 500)
        World.add(save_button)
        level = Level(self.gamestates, self.path.split('\\')[-1][:-4])
        World.setup_level(level)
        thread_lock.pause_main = False
        self.gamestates.state = self.gamestates.BUILDER
        if Borders.focus_object is None:
            Borders.gain_focus(World.main_character)
        Borders.lock()
        pygame.event.set_grab(Settings.mouse_confined)
        self.gamestates.sleep()

    def click_rename(self):
        name = input('New name: ')
        p = Level.default_path + '\\' + name + '.txt'
        os.rename(self.path, p)
        self.path = p
        World.remove(self.name_label)
        self.display_name()
        print('Saved as: ' + p)

    def click_delete(self):
        os.remove(self.path)
        self.back()

    def click_back(self):
        self.back()

    def begin(self):
        self.display_name()

    def end(self):
        World.remove(self.name_label)

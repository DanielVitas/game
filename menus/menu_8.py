from frame.borders import Borders
from frame.image_library import ImageLibrary
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.invisible_button import InvisibleButton
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.text_holders.level_name import LevelName
from physics.coordinates import Coordinates
from thread_lock import target_fps
from objects.game_object.dinamic.characters.cat import Cat
from objects.game_object.dinamic.characters.kirito import Kirito
from objects.game_object.dinamic.characters.marjan import Marjan
from objects.game_object.dinamic.characters.pretnar import Pretnar
from objects.game_object.dinamic.characters.martinator import Martinator
from objects.game_object.dinamic.characters.feguros import Feguros
from objects.game_object.dinamic.characters.batejgrid import Batejgrid


class Menu_8(Menu):
    dim = Coordinates(100, 100)
    blank = Coordinates(70, 50)
    grid = [Coordinates(80, 120), Coordinates(700, 400)]

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 8, 4)
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(10, 10), self.click_back),
                       MenuTextButton('Previous', 30, Coordinates(10, 15), Coordinates(580, 540), self.click_previous),
                       MenuTextButton('Next', 30, Coordinates(10, 15), Coordinates(690, 540), self.click_next),
                       Background('resources\\test_images\\white_background.png')])
        self.characters = []
        self.buttons = []
        self.c = 0
        self.s = 12
        self.name_label = None
        self.character_names = self.get_all_characters()

    def display_name(self):
        name = Settings.main_character_name
        lname = LevelName('Character selected:   ' + name, 30, Coordinates(200, 50))
        self.name_label = lname
        World.add(lname)

    def click_back(self):
        self.back()

    def get_all_characters(self):
        l = []
        for i in ImageLibrary.get_all_file_paths('objects\\game_object\\dinamic\\characters'):
            if i[-3:] == '.py':
                a = i.split('\\')[-1][:-3]
                l.append(a[0].upper() + a[1:])
        return l

    def click_previous(self):
        if self.c >= self.s:
            self.remove_characters()
            self.c -= self.s
            self.add_characters(self.character_names, self.c, len(self.character_names))
        else:
            print('Reached the beginning of characters.')

    def current(self):
        self.remove_characters()
        self.add_characters(self.character_names, self.c, len(self.character_names))

    def click_next(self):
        if self.c + self.s < len(self.character_names):
            self.remove_characters()
            self.c += self.s
            self.add_characters(self.character_names, self.c, len(self.character_names))
        else:
            print('Reached the end of characters.')

    def remove_characters(self):
        for i in self.characters:
            World.remove(i)
        for i in self.buttons:
            World.remove(i)

    def add_characters(self, arr, starting_index, finishing_index):
        g = self.generate_characters(arr, starting_index, finishing_index)
        i = next(g)
        while i[0]:
            self.characters.append(i[0])
            World.add(i[0])
            self.buttons.append(i[1])
            World.add(i[1])
            i = next(g)

    def get_change_function(self, name):
        def f():
            Settings.main_character_name = name
            Settings.write_settings()
            World.remove(self.name_label)
            self.display_name()
#            print('Character selected: ' + name)
        return f

    def generate_characters(self, arr, starting_index, finishing_index):
        if starting_index >= len(arr):
            yield False, False
        if finishing_index > len(arr):
            finishing_index = len(arr)
        l = arr[starting_index: finishing_index]
        g = self.generate_coordinates()
        for i in l:
            c = next(g)
            if c:
                character = eval('%s().construct([Coordinates(1, 1)])' % i)
                character.coordinates = c
                character.type += ['fixed', 'unstretchable']
                character.change_scale(self.dim / Coordinates(50, 50))
                b = InvisibleButton(c, self.get_change_function(i), self.dim.x, self.dim.y)
                yield character, b
            else:
                yield False, False
        yield False, False

    def generate_coordinates(self):
        i = 0
        j = 0
        while (self.dim.y + self.blank.y) * (j + 1) < self.grid[1].y:
            yield self.grid[0] + Coordinates((self.dim.x + self.blank.x) * i, (self.dim.y + self.blank.y) * j)
            i += 1
            if (self.dim.x + self.blank.x) * (i + 1) > self.grid[1].x:
                i = 0
                j += 1
        yield False

    def begin(self):
        self.character_names = self.get_all_characters()
        self.current()
        self.display_name()

    def end(self):
        World.remove(self.name_label)
        self.remove_characters()

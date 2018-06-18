from frame.borders import Borders
from frame.image_library import ImageLibrary
from frame.world import World
from input.key_log.key_logger import KeyLogger
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_6(Menu):
    dim = Coordinates(200, 50)
    blank = Coordinates(10, 10)
    grid = [Coordinates(100, 100), Coordinates(700, 400)]

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 6, 5)  # 0 - quit
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(10, 10), self.click_back),
                       MenuTextButton('Previous', 30, Coordinates(10, 15), Coordinates(580, 540), self.click_previous),
                       MenuTextButton('Next', 30, Coordinates(10, 15), Coordinates(690, 540), self.click_next),
                       Background('resources\\test_images\\white_background.png')])
        self.buttons = []
        self.c = 0
        self.s = 18
        self.paths = self.get_level_paths()

    def click_back(self):
        self.back()

    def click_previous(self):
        if self.c >= self.s:
            self.remove_buttons()
            self.c -= self.s
            self.add_buttons(self.paths, self.c, len(self.paths))
        else:
            print('Reached the beginning of levels.')

    def current(self):
        self.remove_buttons()
        self.add_buttons(self.paths, self.c, len(self.paths))

    def click_next(self):
        if self.c + self.s < len(self.paths):
            self.remove_buttons()
            self.c += self.s
            self.add_buttons(self.paths, self.c, len(self.paths))
        else:
            print('Reached the end of levels.')

    def get_level_paths(self):
        return ImageLibrary.get_all_file_paths('files\\levels')

    def remove_buttons(self):
        for i in self.buttons:
            World.remove(i)

    def add_buttons(self, arr, starting_index, finishing_index):
        g = self.generate_buttons(arr, starting_index, finishing_index)
        i = next(g)
        while i:
            self.buttons.append(i)
            World.add(i)
            i = next(g)

    def get_level_function(self, path):
        def f():
            self.gamestates.menu_library.menus[7].path = path
            self.change_to(7)
        return f

    def generate_buttons(self, arr, starting_index, finishing_index):
        if starting_index >= len(arr):
            yield False
        if finishing_index > len(arr):
            finishing_index = len(arr)
        l = arr[starting_index: finishing_index]
        g = self.generate_coordinates()
        for i in l:
            c = next(g)
            if c:
                yield MenuTextButton(i.split('\\')[-1][:-4], 30, Coordinates(10, 15), c, self.get_level_function(i),
                                     self.dim / Coordinates(100, 50))
            else:
                yield False
        yield False

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
        self.paths = self.get_level_paths()
        self.current()

    def end(self):
        self.remove_buttons()

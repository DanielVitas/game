from frame.borders import Borders
from frame.settings import Settings
from frame.world import World
from input.key_log.key_logger import KeyLogger
from input.key_log.mouse import Mouse
from main_game.menu import Menu
from objects.game_object.static.background import Background
from objects.widgets.buttons.menu_text_button import MenuTextButton
from objects.widgets.text_holders.level_name import LevelName
from physics.coordinates import Coordinates
from thread_lock import target_fps


class Menu_12(Menu):
    dim = Coordinates(280, 50)
    dim_button = Coordinates(130, 50)
    blank = Coordinates(50, 10)
    grid = [Coordinates(100, 100), Coordinates(700, 400)]

    def __init__(self, gamestates):
        Menu.__init__(self, gamestates, 12, 11)
        self.add_list([MenuTextButton('Back', 30, Coordinates(10, 15), Coordinates(10, 10), self.click_back),
                       MenuTextButton('Previous', 30, Coordinates(10, 15), Coordinates(580, 540), self.click_previous),
                       MenuTextButton('Next', 30, Coordinates(10, 15), Coordinates(690, 540), self.click_next),
                       Background('resources\\test_images\\white_background.png')])
        self.buttons = []
        self.c = 0
        self.s = 12
        self.binding_list = None

    def click_previous(self):
        if self.c >= self.s:
            self.remove_buttons()
            self.c -= self.s
            self.add_buttons(self.binding_list, self.c, len(self.binding_list))
        else:
            print('Reached the beginning of bindings.')

    def current(self):
        self.remove_buttons()
        self.add_buttons(self.binding_list, self.c, len(self.binding_list))

    def click_next(self):
        if self.c + self.s < len(self.binding_list):
            self.remove_buttons()
            self.c += self.s
            self.add_buttons(self.binding_list, self.c, len(self.binding_list))
        else:
            print('Reached the end of bindings.')

    def remove_buttons(self):
        for i in self.buttons:
            World.remove(i)

    def add_buttons(self, arr, starting_index, finishing_index):
        g = self.generate_buttons(arr, starting_index, finishing_index)
        i = next(g)
        while i:
            self.buttons.append(i[0])
            self.buttons.append(i[1])
            World.add(i[0])
            World.add(i[1])
            i = next(g)

    def get_key_pressed(self):
        for key in KeyLogger.keys.values():
            if key.check():
                return key
        for key in [Mouse.buttons[2], Mouse.buttons[3]]:
            if key.check():
                return key
        return Mouse.buttons[1]

    def get_binding_list(self):
        return list(KeyLogger.bindings.values())

    def get_binding_function(self, name):
        def f():
            b = self.get_key_pressed()
            if b is not None:
                KeyLogger.bindings[name].key = b
            KeyLogger.write_bindings()
            self.binding_list = self.get_binding_list()
            self.current()
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
                n = LevelName(i.name, 30, c + Coordinates(0, 15))
                b = MenuTextButton(i.key.get_name(), 30, Coordinates(10, 15),
                                   c + (self.dim - self.dim_button) * Coordinates(1, 0),
                                   self.get_binding_function(i.name), self.dim_button / Coordinates(100, 50))
                yield n, b
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

    def click_back(self):
        self.back()

    def begin(self):
        self.binding_list = self.get_binding_list()
        self.current()

    def end(self):
        self.remove_buttons()

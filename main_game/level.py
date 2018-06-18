import os

from frame.settings import Settings
from main_game.game_states import GameStates
from physics.coordinates import Coordinates
from frame.world import World
from frame.borders import Borders
from objects.game_object.dinamic.characters.kirito import Kirito
from objects.game_object.dinamic.obstacles.blocks.grey_block import GreyBlock
from objects.game_object.dinamic.obstacles.targets.classic_target import ClassicTarget
from objects.game_object.dinamic.spawn import Spawn
from objects.game_object.dinamic.obstacles.blocks.shootable_block import ShootableBlock


class Level(object):
    default_path = 'files\\levels'

    def __init__(self, gamestates, name='test_level', additional_path=None):
        self.gamestates = gamestates
        if additional_path is None:
            self.path = Level.default_path + '\\' + name + '.txt'
        else:
            self.path = Level.default_path + additional_path + '\\' + name + '.txt'
        self.world = list()
        self.name = name
        try:
            self.load_preset(self.path)
        except FileNotFoundError:
            print('Created blank.')
            spawn = Spawn()
            spawn.coordinates = Coordinates(0, 0)
            self.add(spawn)
        self.spawn = None
        self.targets = []

    def remove_target(self, target):
        try:
            self.targets.remove(target)
        except ValueError:
            pass
        if not self.targets and self.gamestates.state == self.gamestates.GAME:
            self.gamestates.victory()

    def get_target_number(self):
        return len(self.targets)

    def load(self):
        for obj in self.world:
            World.add(obj)
            if 'spawn' in obj.type:
                self.spawn = obj
            if 'target' in obj.type:
                self.targets.append(obj)
        GameStates.spawn(self.spawn.get_coordinates())

    def write(self, name=None, additional_path=None, world=None):
        if world is None:
            world = World.writable
        if name is None:
            name = self.name
        if name == '':
            name = input('Enter level name: ')
            self.name = name
        if additional_path is None:
            s = Level.default_path + '\\' + name + '.txt'
        else:
            s = Level.default_path + '\\' + additional_path + name + '.txt'
        print('Saved as:', s)
        with open(s, 'w') as file:
            for obj in world:
                prefix = '-'
                coordinates = obj.get_coordinates()
                coordinates = Coordinates(int(coordinates.x), int(coordinates.y))
                args = obj.get_args()
                if not args:
                    args = '-'
                object_type = obj.__class__.__name__
                file.write(prefix + '; ' + str(object_type) + '; ' + str(coordinates.get()) + '; ' + str(args) + '\n')

    def load_preset(self, path):
        with open(path) as file:
            for line in file:
                a = line.split('; ')
                if a[0] == '#':
                    pass
                elif a[0] == '-':
                    if a[3] in ['-\n', '-']:
                        self.create(a[1], a[2])
                    else:
                        self.create(a[1], a[2], a[3])

    def create(self, obj, coord='(0, 0)', args=''):
        code = '%s.construct(%s)' % (obj, args)
        game_object = eval(code)
        coordinates = coord[1: -1].split(', ')
        game_object.coordinates = Coordinates(int(coordinates[0]), int(coordinates[1]))
        self.add(game_object)
        return game_object

    def spawn_character(self, main_character=None):
        if main_character is None:
            main_character = Settings.main_character_name
        GameStates.spawn(self.spawn.get_coordinates(), main_character)

    def add(self, game_object):
        self.world.append(game_object)


if __name__ == '__main__':
    pass

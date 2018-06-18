from objects.game_object.game_object import GameObject
from objects.images.static_animation import StaticAnimation


class Spawn(GameObject):

    def __init__(self):
        GameObject.__init__(self, [StaticAnimation(self, 'resources\\test_images\\spawn.png')])
        self.character = 'Kirito'
        self.type.append('writable')
        self.type.append('spawn')
        self.priority = 10
        self.width = 50
        self.height = 50

    @staticmethod
    def construct(args):
        g = Spawn()
        g.base_construct([args[0]])
        return g

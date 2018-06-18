from objects.game_object.dinamic.obstacles.block import Block
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates


class ShootableBlock(Block):

    def __init__(self, a, b):
        Block.__init__(self, [StaticAnimation(self, 'resources\\test_images\\turquoise.png', Coordinates(a, b),
                                              name='obstacle')], a, b)
        self.args += [a, b]
        self.type.append('shootable')

    @staticmethod
    def construct(args):
        g = ShootableBlock(int(args[1]), int(args[2]))
        g.base_construct([args[0]])
        return g

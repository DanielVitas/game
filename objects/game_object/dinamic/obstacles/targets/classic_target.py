from objects.game_object.dinamic.obstacles.target import Target
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.rectangle import Rectangle


class ClassicTarget(Target):

    def __init__(self):
        a = 50
        b = a
        Target.__init__(self, [StaticAnimation(self, 'resources\\test_images\\target.png', Coordinates(a, b), name='target')])
        self.hitboxes = [Rectangle(self, Coordinates(0, 0), a, b)]
        self.width = a
        self.height = b

    @staticmethod
    def construct(args):
        g = ClassicTarget()
        g.base_construct([args[0]])
        return g

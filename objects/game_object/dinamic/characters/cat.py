from objects.game_object.dinamic.character import Character
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates


class Cat(Character):

    def __init__(self):
        Character.__init__(self, [StaticAnimation(self, 'resources\\test_images\\characters\\cat.png')])
        self.additional_firing_coordinates = Coordinates(25, 25)
        self.width = 50
        self.height = 50

    @staticmethod
    def construct(args):
        g = Cat()
        g.base_construct([args[0]])
        return g

from objects.game_object.game_object import GameObject
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from frame.settings import Settings


class Background(GameObject):

    def __init__(self, path):
        GameObject.__init__(self, [StaticAnimation(self, path)])
        self.type.append('fixed')
        self.type.append('unstretchable')
        self.coordinates = Coordinates(0, 0)
        self.priority = 0

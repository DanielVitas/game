from objects.game_object.game_object import GameObject
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates


class ShootMarker(GameObject):

    def __init__(self):
        GameObject.__init__(self, [StaticAnimation(self, 'resources\\test_images\\red.png'), Coordinates(5, 5)])
        self.priority = 100
        self.width = 5
        self.height = 5

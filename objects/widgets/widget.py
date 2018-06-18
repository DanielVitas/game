from frame.world import World
from physics.coordinates import Coordinates
from frame.frame import Frame


class Widget(object):

    def __init__(self, animations):
        self.coordinates = Coordinates(0, 0)
        self.scale = Coordinates(1, 1)
        self.type = ['widget', 'fixed', 'unstretchable']
        self.priority = 200
        self.animations = animations
        self.width = 0
        self.height = 0

    def get_coordinates(self):
        return self.coordinates

    def world_remove(self):
        World.remove(self)

    def reposition(self, coordinates):
        self.coordinates = coordinates

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def stretch(self, scale):
        self.height *= scale.y
        self.width *= scale.x

    def change_scale(self, scale):
        if scale.x > 0 and scale.y > 0:
            self.stretch(Coordinates(1, 1) / self.scale)
            self.scale = scale
            self.stretch(self.scale)
        else:
            self.world_remove()

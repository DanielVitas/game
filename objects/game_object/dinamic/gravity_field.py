from objects.game_object.game_object import GameObject
from physics.coordinates import Coordinates
from frame.frame import Frame


class GravityField(GameObject):

    def __init__(self, animations, mass):
        GameObject.__init__(self, animations)
        self.type.append('gravity field')
        self.mass = mass
        self.center_of_gravity = Coordinates(0, 0)

    def get_center_of_gravity(self):
        return self.get_coordinates() + self.center_of_gravity * Frame.scale

    def hit(self):
        pass

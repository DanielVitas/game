from objects.game_object.dinamic.gravity_field import GravityField
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.circle import Circle


class NormalGravityField(GravityField):

    def __init__(self):
        GravityField.__init__(self, [StaticAnimation(self, 'resources\\test_images\\normal_gravity_field.png')], 8 * 10 ** 13)
        self.center_of_gravity = Coordinates(12.5, 12.5)
        self.hitboxes = [Circle(self, self.center_of_gravity, 12.5)]
        self.width = 25
        self.height = 25

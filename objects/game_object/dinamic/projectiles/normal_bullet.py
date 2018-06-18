from objects.game_object.dinamic.projectile import Projectile
from objects.images.static_animation import StaticAnimation
from physics import constants
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.rectangle import Rectangle
from frame.world import World


class NormalBullet(Projectile):
    normal_velocity = 10  # m / s

    def __init__(self, direction):
        starting_velocity = direction * NormalBullet.normal_velocity * constants.meter_to_pixel
        Projectile.__init__(self, [StaticAnimation(self, 'resources\\test_images\\bullet.png')], starting_velocity,
                            Coordinates(2.5, 2.5), 0.04)
        self.hitboxes = [Rectangle(self, Coordinates(0, 0), 5, 5)]
        self.hit_exceptions = [World.main_character]


if __name__ == '__main__':
    from physics.vector import Vector

    a = NormalBullet(1)
    b = NormalBullet(Vector(0, 0))

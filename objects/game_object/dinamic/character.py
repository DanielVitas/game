from objects.game_object.game_object import GameObject
from objects.game_object.dinamic.projectiles.normal_bullet import NormalBullet
from frame.world import World
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.rectangle import Rectangle
from physics.vector import Vector
from thread_lock import target_fps


class Character(GameObject):

    def __init__(self, animations):
        GameObject.__init__(self, animations)
        self.type.append('hittable')
        self.hitboxes = [Rectangle(self, Coordinates(0, 0), 50, 50)]
        self.priority = 80
        self.walking_distance = Coordinates(600, 600)
        self.additional_firing_coordinates = Coordinates(0, 0)

    def damage(self):
        pass

    def fire_normal_bullet(self, direction):
        bullet = NormalBullet(direction)
        bullet.coordinates = self.get_firing_coordinates()
        World.add(bullet)

    def move(self, direction):
        v = self.walking_distance / target_fps * direction
        try:
            d = self.get_safe_distance(v)
        except RecursionError:
            print('Maximum recursion depth exceeded.')
            d = Vector(0, 0)
        self.reposition(self.coordinates + d)

    def get_safe_distance(self, v, k=0):
        if k > 2:
            return Coordinates(0, 0)
        o = self.check_collision(v, type_exceptions=['walkable'])
        if o is not None:
            k += 1
            d = Vector(v).normalize() * (Vector(self.distance(o, v)) * Vector(v).normalize())
            return self.get_safe_distance((Coordinates(d) * Coordinates(0.99, 0.99)).int(), k)
        else:
            return v

    def get_firing_coordinates(self):
        return self.get_coordinates() + self.additional_firing_coordinates

    def hit(self):
        pass


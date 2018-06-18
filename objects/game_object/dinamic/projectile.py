from objects.game_object.game_object import GameObject
from physics.vector import Vector
from physics.coordinates import Coordinates
from frame.world import World
from physics import constants
from threads.thread import Thread
from frame.frame import Frame
import thread_lock
from thread_lock import target_fps


class Projectile(GameObject):

    def __init__(self, animations, velocity=Vector(0, 0), center_of_gravity=Coordinates(0, 0), mass=0.02):
        GameObject.__init__(self, animations)
        self.velocity = velocity
        self.mass = mass
        self.hit_exceptions = []
        self.type_exceptions = ['shootable']
        self.center_of_gravity = center_of_gravity
        self.thread = Thread(self.run, (), 'projectile thread')

    def run(self):
        self.move()

    def move(self):
        if not thread_lock.pause_main:
            dt = 1 / target_fps
            a = self.gravity()
            additional_coordinates = self.velocity * dt + a * (dt ** 2 / 2)
            c = self.check_collision(additional_coordinates, self.hit_exceptions, self.type_exceptions)
            if c is None:
                self.reposition(self.get_coordinates() + additional_coordinates)
                self.velocity += a * dt
            else:
                c.hit()
                self.world_remove()
                self.thread.stop()

    def gravity(self):
        v = Vector(0, 0)
        for field in World.gravity_fields:
            v += self.newton_g(field)
        return v

    def get_center_of_gravity(self):
        return self.coordinates + self.center_of_gravity * Frame.scale

    def newton_g(self, field):
        r = Vector(field.get_center_of_gravity() - self.get_center_of_gravity())
        return r * (self.mass * field.mass / abs(r) ** 3 * constants.G)

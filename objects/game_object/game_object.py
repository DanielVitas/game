from physics.coordinates import Coordinates
from frame.world import World


class GameObject(object):

    def __init__(self, animations):
        self.args = [Coordinates(1, 1)]
        self.type = []
        self.scale = Coordinates(1, 1)
        self.hitboxes = list()
        self.coordinates = Coordinates(0, 0)
        self.animations = animations
        self.priority = 100
        self.width = 0
        self.height = 0
        self.texts = []

    def collides(self, other, additional_coordinates=Coordinates(0, 0), type='simple'):
        if additional_coordinates == Coordinates(0, 0) or type == 'simple':
            for h1 in self.hitboxes:
                for h2 in other.hitboxes:
                    if h1.collides(h2, additional_coordinates):
                        return True
            return False
        else:
            for h1 in self.hitboxes:
                for h2 in other.hitboxes:
                    if h1.future_collision(h2, additional_coordinates):
                        return True
            return False

    def check_collision(self, additional_coordinates=Coordinates(0, 0), hit_exceptions=[], type_exceptions=[],
                        type='simple'):
        hit_exceptions += [self]
        for gravity_field in World.gravity_fields:
            if not [x for x in gravity_field.type if x in type_exceptions]:
                if self.collides(gravity_field, additional_coordinates) and gravity_field not in hit_exceptions:
                        return gravity_field
        for game_object in World.hittable:
            if not [x for x in game_object.type if x in type_exceptions]:
                if self.collides(game_object, additional_coordinates) and game_object not in hit_exceptions:
                    return game_object

    def get_args(self):
        return self.args

    def get_coordinates(self):
        return self.coordinates

    def reposition(self, coordinates):
        self.coordinates = coordinates

    def world_remove(self):
        World.remove(self)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def distance(self, other, v, additional_coordinates=Coordinates(0, 0)):
        d = v
        for hitbox1 in self.hitboxes:
            for hitbox2 in other.hitboxes:
                a = hitbox1.distance(hitbox2, additional_coordinates)
                if abs(a) < abs(d):
                    d = a
        return d

    def stretch(self, scale):
        self.height *= scale.y
        self.width *= scale.x
        for hitbox in self.hitboxes:
            hitbox.stretch(scale)

    def change_scale(self, scale):
        if scale.x > 0 and scale.y > 0:
            self.stretch(Coordinates(1, 1) / self.scale)
            self.scale = scale
            self.args[0] = scale
            self.stretch(self.scale)
        else:
            self.world_remove()

    def add_scale(self, additional_scale):
        self.change_scale(self.scale + additional_scale)

    def base_construct(self, base_args):
        self.change_scale(base_args[0])
        self.args[0] = self.scale

from objects.game_object.hitboxes.hitbox import Hitbox
from physics.coordinates import Coordinates
from physics.vector import Vector
from objects.game_object.hitboxes.multiline_object import MultilineObject


class Circle(Hitbox):

    def __init__(self, gameobject, coordinates, radius):
        Hitbox.__init__(self, gameobject, coordinates)
        self.type = 'circle'
        self.radius = radius

    def stretch(self, scale):
        self.coordinates *= scale
        self.radius *= scale

    def distance(self, other, additional_coordinates):
        if other.type == 'circle':
            return self.distance_circle(other, additional_coordinates)
        if other.type == 'line':
            return other.distance(self, additional_coordinates * (-1)) * (-1)
        if other.type == 'rectangle':
            return self.distance_rectangle(other, additional_coordinates)

    def distance_circle(self, other, additional_coordinates):
        d = other.get_coordinates() - self.get_coordinates() - additional_coordinates
        return d * (abs(d) - self.radius - other.radius)

    def distance_rectangle(self, other, additional_coordinates):
        lines = other.get_lines()
        d = self.distance(lines[0], additional_coordinates)
        for line in lines[1:]:
            a = self.distance(line, additional_coordinates)
            if abs(a) < abs(d):
                d = a
        return d

    def collides(self, other, additional_coordinates=Coordinates(0, 0)):
        if other.type == 'circle':
            return self.collides_circle(other, additional_coordinates)
        elif other.type in ['rectangle', 'line', 'multiline_object']:
            return other.collides(self, additional_coordinates * (-1))

    def collides_circle(self, other, additional_coordinates):
        if abs(self.get_coordinates() + additional_coordinates - other.get_coordinates()) <= self.radius + other.radius:
            return True
        return False

    def get_y(self, x):
        x = x - self.get_coordinates().x
        if x ** 2 > self.radius ** 2:
            return []
        y_ = (self.radius ** 2 - x ** 2) ** (1 / 2)
        if y_ == 0:
            return [self.get_coordinates().y]
        return [self.get_coordinates().y + y_, self.get_coordinates().y - y_]

    def get_x(self, y):
        y = y - self.get_coordinates().y
        if y ** 2 > self.radius ** 2:
            return []
        x_ = (self.radius ** 2 - y ** 2) ** (1 / 2)
        if x_ == 0:
            return [self.get_coordinates().x]
        return [self.get_coordinates().x + x_, self.get_coordinates().x - x_]

    def get_intersections(self, line):
        a = line.e * line.e
        if a == 0:
            return []
        b = 2 * (line.e.x * (line.get_coordinates().x - self.get_coordinates().x) + line.e.y *
                 (line.get_coordinates().y + self.get_coordinates().y))
        c = (line.get_coordinates().x - self.get_coordinates().x) ** 2 +\
            (line.get_coordinates().y + self.get_coordinates().y) ** 2 - self.radius ** 2
        d = b ** 2 - 4 * a * c
        if d < 0:
            return []
        elif d == 0:
            lam = -b / (2 * a)
            return [line.get_coordinates() + line.e * lam]
        else:
            lam1 = (-b + d ** (1 / 2)) / (2 * a)
            lam2 = (-b - d ** (1 / 2)) / (2 * a)
            return [line.get_coordinates() + line.e * lam1, line.get_coordinates() + line.e * lam2]

    def is_inside(self, other):
        return abs(self.get_coordinates() - other.get_coordinates()) <= self.radius

    def future_shape(self, additional_coordinates):
        circle2 = Circle(self.gameobject, self.get_coordinates() + additional_coordinates, self.radius)
        v = Vector(additional_coordinates).normalize().right_angled()
        line1 = Line(self.gameobject, self.get_coordinates() + v * self.radius,
                     self.get_coordinates() - v * self.radius)
        line2 = Line(self.gameobject, self.get_coordinates() - v * self.radius,
                     self.get_coordinates() - v * self.radius + additional_coordinates)
        line3 = Line(self.gameobject, self.get_coordinates() - v * self.radius + additional_coordinates,
                     self.get_coordinates() + v * self.radius + additional_coordinates)
        line4 = Line(self.gameobject, self.get_coordinates() + v * self.radius + additional_coordinates,
                     self.get_coordinates() + v * self.radius)
        return [self, circle2, MultilineObject(self.gameobject, self.coordinates, [line1, line2, line3, line4])]


if __name__ == '__main__':
    from objects.game_object.game_object import GameObject
    from physics.coordinates import Coordinates
    from objects.game_object.hitboxes.line import Line

    g = GameObject([])
    g.coordinates = Coordinates(5, 0)
    c = Circle(g, Coordinates(1, 0), 5)
    l = Line(g, Coordinates(2, 0), Coordinates(2, 0))

    print(c.get_intersections(l))

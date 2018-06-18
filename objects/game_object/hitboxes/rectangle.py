from objects.game_object.hitboxes.hitbox import Hitbox
from objects.game_object.hitboxes.line import Line
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.multiline_object import MultilineObject


class Rectangle(Hitbox):

    def __init__(self, gameobject, coordinates, a, b):
        Hitbox.__init__(self, gameobject, coordinates)
        self.type = 'rectangle'
        self.a = a
        self.b = b

    def stretch(self, scale):
        self.coordinates *= scale
        self.a *= scale.x
        self.b *= scale.y

    def distance(self, other, additional_coordinates):
        if other.type == 'rectangle':
            return self.distance_rectangle(other, additional_coordinates)
        if other.type in ['line', 'circle']:
            return other.distance(self, additional_coordinates * (-1)) * (-1)

    def distance_rectangle(self, other, additional_coordinates):
        lines = self.get_lines()
        d = lines[0].distance(other, additional_coordinates)
        for line in lines[1:]:
            a = line.distance(other, additional_coordinates)
            if abs(a) < abs(d):
                d = a
        return d

    def collides(self, other, additional_coordinates=Coordinates(0, 0)):
        if other.type == 'rectangle':
            return self.collides_rectangle(other, additional_coordinates)
        elif other.type == 'circle':
            return self.collides_circle(other, additional_coordinates)
        elif other.type in ['line', 'multiline_object']:
            return other.collides(self, additional_coordinates * (-1))

    def collides_rectangle(self, other, additional_coordinates):
        c1 = self.get_coordinates() + additional_coordinates
        c2 = other.get_coordinates()
        if c1.x > c2.x + other.a:
            return False
        if c1.x + self.a < c2.x:
            return False
        if c1.y > c2.y + other.b:
            return False
        if c1.y + self.b < c2.y:
            return False
        return True

    def collides_circle(self, other, additional_coordinates):
        c1 = self.get_coordinates() + additional_coordinates
        c2 = other.get_coordinates()
        y_ = other.get_y(c1.x)
        for y in y_:
            if c1.y <= y <= c1.y + self.b:
                return True
        y_ = other.get_y(c1.x + self.a)
        for y in y_:
            if c1.y <= y <= c1.y + self.b:
                return True
        x_ = other.get_x(c1.y)
        for x in x_:
            if c1.x <= x <= c1.x + self.a:
                return True
        x_ = other.get_x(c1.y + self.b)
        for x in x_:
            if c1.x <= x <= c1.x + self.a:
                return True
        return abs(c1 - c2) <= other.radius

    def get_lines(self):
        line1 = Line(self.gameobject, self.coordinates, self.coordinates + Coordinates(0, self.b))
        line2 = Line(self.gameobject, self.coordinates + Coordinates(0, self.b), self.coordinates +
                     Coordinates(self.a, self.b))
        line3 = Line(self.gameobject, self.coordinates + Coordinates(self.a, self.b), self.coordinates +
                     Coordinates(self.a, 0))
        line4 = Line(self.gameobject, self.coordinates + Coordinates(self.a, 0), self.coordinates)
        return [line1, line2, line3, line4]

    def future_shape(self, additional_coordinates):
        lines = self.get_lines()
        for i in [1, 2]:
            lines[i].coordinates += additional_coordinates
        side_line1 = Line(self.gameobject, self.coordinates + Coordinates(0, self.b),
                          self.coordinates + Coordinates(0, self.b) + additional_coordinates)
        side_line2 = Line(self.gameobject, self.coordinates + additional_coordinates + Coordinates(self.a, 0),
                          self.coordinates + Coordinates(self.a, 0))
        return [MultilineObject(self.gameobject, self.coordinates, lines + [side_line1, side_line2])]


if __name__ == '__main__':
    from objects.game_object.game_object import GameObject
    from physics.coordinates import Coordinates

    g = GameObject([])
    g.coordinates = Coordinates(0, 0)
    r1 = Rectangle(g, Coordinates(0, 0), 1, 1)
    r2 = Rectangle(g, Coordinates(0.5, -2), 1, 20)
    print(r1.distance(r2, Coordinates(0, 0)))


from physics.vector import Vector


class Coordinates(object):

    def __init__(self, x, y=None):
        if y is not None:
            self.x = x
            self.y = y
        else:
            self.x = x.x
            self.y = x.y

    def __add__(self, other):
        if type(other) == Vector:
            other = Coordinates(other.x, other.y)
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) == Vector:
            other = Coordinates(other.x, other.y)
        return Coordinates(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) in [Coordinates, Vector]:
            return Coordinates(self.x * other.x, self.y * other.y)
        elif type(other) in [int, float]:
            return Coordinates(self.x * other, self.y * other)

    def __truediv__(self, other):
        if type(other) in [Coordinates, Vector]:
            return Coordinates(self.x / other.x, self.y / other.y)
        elif type(other) == int:
            return Coordinates(self.x / other, self.y / other)

    def __repr__(self):
        return 'Coordinates' + str((self.x, self.y))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def distance(self, other):
        if other.type == 'circle':
            return self.distance_circle(other)
        elif other.type == 'line':
            return self.distance_line(other)
        elif other.type == 'rectangle':
            return self.distance_rectangle(other)

    def distance_circle(self, other):
        v = other.get_coordinates() - self
        return v * (abs(v) - other.radius)

    def distance_line(self, other):
        c = Vector(self - other.get_coordinates())
        lam = (c * other.e) / (other.e * other.e)
        if lam <= 0:
            return c * (-1)
        elif lam >= 1:
            return other.e - c
        else:
            eps = (c ** other.e) / (other.e * other.e)
            return other.e.right_angled() * eps * (-1)

    def distance_rectangle(self, other):
        c = other.get_coordinates()
        if self.x < c.x:
            if self.y < c.y:
                return Vector(c - self)
            elif self.y > c.y + other.b:
                return Vector(c + Coordinates(0, other.b) - self)
            else:
                return self.distance(other.get_lines()[0])
        elif self.x > c.x + other.a:
            if self.y < c.y:
                return Vector(c + Coordinates(other.a, 0) - self)
            elif self.y > c.y + other.b:
                return Vector(c + Coordinates(other.a, other.b) - self)
            else:
                return self.distance(other.get_lines()[2])
        else:
            if self.y < c.y:
                return self.distance(other.get_lines()[3])
            elif self.y > c.y + other.b:
                return self.distance(other.get_lines()[1])
            else:
                return Vector(0, 0)

    def int(self):
        return Coordinates(int(self.x), int(self.y))

    def get(self):
        return self.x, self.y

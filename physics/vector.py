class Vector(object):

    def __init__(self, x, y=None):
        if y is not None:
            self.x = x
            self.y = y
        else:
            self.x = x.x
            self.y = x.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        if type(other) == int or float:
            return Vector(self.x * other, self.y * other)

    def __repr__(self):
        return 'Vector' + str((self.x, self.y))

    def __abs__(self):
        return (self * self) ** (1 / 2)

    def __pow__(self, power, modulo=None):
        return self.x * power.y - self.y * power.x

    def right_angled(self):
        return Vector(self.y, -self.x)

    def normalize(self):
        if self.x != 0 or self.y != 0:
            return self * (1 / abs(self))
        else:
            return self


if __name__ == '__main__':
    print(Vector(1, 2) * 3)
    print(Vector(1, 2) * Vector(2, 2))

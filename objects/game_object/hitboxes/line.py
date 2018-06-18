from objects.game_object.hitboxes.hitbox import Hitbox
from physics.vector import Vector
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.multiline_object import MultilineObject


class Line(Hitbox):

    def __init__(self, gameobject, coordinates, finishing_coordinates):
        Hitbox.__init__(self, gameobject, coordinates)
        self.type = 'line'
        self.e = Vector(finishing_coordinates - coordinates)

    def stretch(self, scale):
        self.coordinates *= scale
        self.e *= scale

    def distance(self, other, additional_coordinates):
        if other.type == 'line':
            return self.distance_line(other, additional_coordinates)
        if other.type == 'circle':
            return self.distance_circle(other, additional_coordinates)
        if other.type == 'rectangle':
            return self.distance_rectangle(other, additional_coordinates)

    def distance_line(self, other, additional_coordinates):
        d = (self.get_coordinates() + additional_coordinates).distance(other)
        for i in [(self.get_coordinates() + additional_coordinates + self.e).distance(other)]:
            if abs(i) < abs(d):
                d = i
        for j in [(other.get_coordinates() - additional_coordinates + other.e).distance(self),
                  (other.get_coordinates() - additional_coordinates).distance(self)]:
            if abs(j) < abs(d):
                d = j * (-1)
        return d

    def distance_circle(self, other, additional_coordinates):
        d = (other.get_coordinates() - additional_coordinates).distance(self)
        return d * (-1)

    def distance_rectangle(self, other, additional_coordinates):
        lines = other.get_lines()
        d = self.distance(lines[0], additional_coordinates)
        for i in lines[1:]:
            a = self.distance(i, additional_coordinates)
            if abs(a) < abs(d):
                d = a
        return d

    def collides(self, other, additional_coordinates=Coordinates(0, 0)):
        if other.type == 'line':
            return self.collides_line(other, additional_coordinates)
        elif other.type == 'circle':
            return self.collides_circle(other, additional_coordinates)
        elif other.type == 'rectangle':
            return self.collides_rectangle(other, additional_coordinates)
        elif other.type == 'multiline_object':
            return other.collides(self, additional_coordinates * (-1))

    def collides_line(self, other, additional_coordinates):
        a = Vector(other.get_coordinates() - self.get_coordinates() - additional_coordinates)
        e1 = self.e
        e2 = other.e
        if e1 ** e2 == 0:
            if a ** e1 != 0:
                return False
            else:
                if a.x == 0:
                    if a.y == 0:
                        return True
                    else:
                        lam1 = a.y / e1.y
                        lam2 = (a.y + e2.y) / e1.y
                        if 0 <= lam1 <= 1 or 0 <= lam2 <= 1:
                            return lam1 * lam2 < 0
                        else:
                            return True
                else:
                    lam1 = a.x / e1.x
                    lam2 = (a.x + e2.x) / e1.x
                    if not 0 <= lam1 <= 1 or 0 <= lam2 <= 1:
                        return lam1 * lam2 < 0
                    else:
                        return True
        else:
            lam1 = (a ** e2) / (e1 ** e2)
            lam2 = (a ** e1) / (e1 ** e2)
            return 0 <= lam1 <= 1 and 0 <= lam2 <= 1

    def collides_circle(self, other, additional_coordinates):
        self.coordinates += additional_coordinates
        previous_lam = 0
        for intersection in other.get_intersections(self):
            t = intersection - self.get_coordinates()
            if t.x == 0:
                if t.y == 0:
                    self.coordinates -= additional_coordinates
                    return True
                else:
                    lam = t.y / self.e.y
                    if 0 <= lam <= 1 or previous_lam * lam < 0:
                        self.coordinates -= additional_coordinates
                        return True
                    previous_lam = lam
            else:
                lam = t.x / self.e.x
                if 0 <= lam <= 1 or previous_lam * lam < 0:
                    self.coordinates -= additional_coordinates
                    return True
                previous_lam = lam
        self.coordinates -= additional_coordinates
        return False

    def collides_rectangle(self, other, additional_coordinates):
        lines = other.get_lines()
        for line in lines:
            if self.collides(line, additional_coordinates):
                return True
        c = self.get_coordinates() + additional_coordinates
        r = other.get_coordinates()
        if not r.x <= c.x <= r.x + other.a:
            return False
        if not r.y <= c.y <= r.y + other.b:
            return False
        return True

    def future_shape(self, additional_coordinates):
        line1 = self
        line2 = Line(self.gameobject, self.get_coordinates() + self.e,
                     self.get_coordinates() + additional_coordinates + self.e)
        line3 = Line(self.gameobject, self.get_coordinates() + additional_coordinates + self.e,
                     self.get_coordinates() + additional_coordinates)
        line4 = Line(self.gameobject, self.get_coordinates() + additional_coordinates,
                     self.get_coordinates())
        return [MultilineObject(self.gameobject, self.get_coordinates(), [line1, line2, line3, line4])]


if __name__ == '__main__':
    from objects.game_object.game_object import GameObject
    from physics.coordinates import Coordinates
    from objects.game_object.hitboxes.rectangle import Rectangle

    g = GameObject([])
    g.coordinates = Coordinates(0, 0)
    l1 = Line(g, Coordinates(1, 1), Coordinates(2, 0))
    c = Coordinates(2, 1)
    print(c.distance(l1))

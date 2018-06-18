from objects.game_object.hitboxes.hitbox import Hitbox
from physics.coordinates import Coordinates


class MultilineObject(Hitbox):  # konkaven veckotnik

    def __init__(self, gameobject, coordinates, lines):
        Hitbox.__init__(self, gameobject, coordinates)
        self.type = 'multiline_object'
        self.lines = lines

    def collides(self, other, additional_coordinates=Coordinates(0, 0)):
        if other.type == 'multiline_object':
            return self.collides_multiline_object(other, additional_coordinates)
        elif other.type == 'circle':
            return self.collides_circle(other, additional_coordinates)
        elif other.type == 'rectangle':
            return self.collides_rectangle(other, additional_coordinates)
        elif other.type == 'line':
            return self.collides_line(other, additional_coordinates)

    def collides_multiline_object(self, other, additional_coordinates):
        for line1 in self.lines:
            for line2 in other.lines:
                if line1.collides(line2, additional_coordinates):
                    return True
        return self.is_inside(other) or other.is_inside(self)

    def collides_circle(self, other, additional_coordinates):
        for line in self.lines:
            if line.collides(other, additional_coordinates):
                return True
        return self.is_inside(other) or other.is_inside(self)

    def collides_rectangle(self, other, additional_coordinates):
        rec = MultilineObject(other.gameobject, other.coordinates, other.get_lines())
        return self.collides(rec, additional_coordinates)

    def collides_line(self, other, additional_coordinates):
        for line in self.lines:
            if line.collides(other, additional_coordinates):
                return True
        return self.is_inside(other)

    def is_inside(self, other):
        y_ = self.get_y(other.get_coordinates().x)
        c = 1
        for y in y_:
            c *= y - other.get_coordinates().y
        if c <= 0:
            return True
        x_ = self.get_x(other.get_coordinates().y)
        c = 1
        for x in x_:
            c *= x - other.get_coordinates().x
        if c <= 0:
            return True
        return False

    def get_y(self, x):
        changed = False
        y1 = 0
        y2 = 0
        for line in self.lines:
            if line.get_coordinates().x <= x <= line.get_coordinates().x + line.e.x:
                if line.e.x != 0:
                    changed = True
                    lam = (x - line.get_coordinates().x) / line.e.x
                    y1 = line.get_coordinates().y + lam * line.e.y
            if line.get_coordinates().x + line.e.x <= x <= line.get_coordinates().x:
                if line.e.x != 0:
                    lam = (x - line.get_coordinates().x) / line.e.x
                    y2 = line.get_coordinates().y + lam * line.e.y
        if not changed:
            return []
        return [y1, y2]

    def get_x(self, y):
        changed = False
        x1 = 0
        x2 = 0
        for line in self.lines:
            if line.get_coordinates().y <= y <= line.get_coordinates().y + line.e.y:
                if line.e.y != 0:
                    changed = True
                    lam = (y - line.get_coordinates().y) / line.e.y
                    x1 = line.get_coordinates().x + lam * line.e.x
            if line.get_coordinates().y + line.e.y <= y <= line.get_coordinates().y:
                if line.e.y != 0:
                    lam = (y - line.get_coordinates().y) / line.e.y
                    x2 = line.get_coordinates().x + lam * line.e.x
        if not changed:
            return []
        return [x1, x2]

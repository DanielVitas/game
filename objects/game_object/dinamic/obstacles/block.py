from objects.game_object.dinamic.obstacle import Obstacle
from physics.coordinates import Coordinates
from objects.game_object.hitboxes.rectangle import Rectangle


class Block(Obstacle):

    def __init__(self, animations, a, b):
        Obstacle.__init__(self, animations)
        self.hitboxes = [Rectangle(self, Coordinates(0, 0), a, b)]
        self.type.append('block')
        self.priority = 90
        self.width = a
        self.height = b

    def hit(self):
        pass

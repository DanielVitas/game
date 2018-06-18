from frame.world import World
from objects.game_object.dinamic.obstacle import Obstacle


class Target(Obstacle):

    def __init__(self, animations):
        Obstacle.__init__(self, animations)
        self.type.append('target')

    def hit(self):
        self.world_remove()
        World.level.remove_target(self)

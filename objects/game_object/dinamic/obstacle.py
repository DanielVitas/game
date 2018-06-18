from objects.game_object.game_object import GameObject


class Obstacle(GameObject):

    def __init__(self, animations):
        GameObject.__init__(self, animations)
        self.type.append('hittable')
        self.type.append('writable')

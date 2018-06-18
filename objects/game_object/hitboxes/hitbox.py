class Hitbox(object):

    def __init__(self, gameobject, coordinates):
        self.type = ''
        self.gameobject = gameobject
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.gameobject.coordinates + self.coordinates

    def future_collision(self, other, additional_coordinates):
        obj = self.future_shape(additional_coordinates)
        for hitbox in obj:
            if hitbox.collides(other):
                return True
        return False

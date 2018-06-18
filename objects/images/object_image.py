from frame.image_library import ImageLibrary
from physics.coordinates import Coordinates


class ObjectImage(object):

    def __init__(self, path, coordinates, scale=Coordinates(1, 1)):
        self.path = path
        self.coordinates = coordinates
        self.scale = scale

    def get_texture(self):
        return ImageLibrary.get_image(self.path).get_texture()

    def get_scale(self):
        return self.scale * ImageLibrary.get_image(self.path).get_scale()

    def get_coordinates(self):
        return self.coordinates

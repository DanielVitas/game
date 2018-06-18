import pygame
from physics.coordinates import Coordinates


class Image(object):

    def __init__(self, path):
        self.path = path
        self.scale = Coordinates(0, 0)
        self.texture = pygame.image.load(path)

    def get_texture(self):
        return self.texture

    def get_scale(self):
        return self.scale

import pygame
from physics.coordinates import Coordinates


class Label(object):

    def __init__(self, text, size=15, color=(0, 0, 0), font='monospaced', antialias=False):
        self.font = pygame.font.SysFont(font, size)
        self.text = text
        self.color = color
        self.antialias = antialias
        self.texture = None
        self.coordinates = Coordinates(0, 0)
        self.create_texture()

    def get_text(self):
        return self.text

    def get_font(self):
        return self.font

    def set_text(self, new_text):
        self.text = new_text
        self.create_texture()

    def get_texture(self):
        return self.texture

    def create_texture(self):
        self.texture = self.font.render(self.text, self.antialias, self.color)

    def get_coordinates(self):
        return self.coordinates

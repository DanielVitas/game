import pygame
from frame.frame import Frame
from frame.settings import Settings
from physics.coordinates import Coordinates
from threads.animation_thread import AnimationThread
from objects.images.animation_library import AnimationLibrary


class Animation(object):

    def __init__(self, obj, images, delay=[], name='generic animation'):
        self.images = images
        self.textures = []
        self.obj = obj
        if not delay:
            delay = [1/3]
        self.delay = delay
        self.counter = 0
        AnimationLibrary.add(self)
        self.thread = AnimationThread(self.run, (), delay, name)

    def get_texture(self):
        try:
            scale = Frame.scale * self.obj.scale
            if 'unstretchable' not in self.obj.type:
                scale *= Settings.frame_additional_scale
            image = self.images[self.counter]
            return pygame.transform.scale(image.get_texture(), (image.get_scale() * scale).int().get())
        except IndexError:
            return None
        except pygame.error:
            print('Width or height is too large.')
            Settings.frame_additional_scale = Coordinates(1, 1)

    def get_coordinates(self):
        return self.images[self.counter].get_coordinates()

    def run(self):
        yield self.get_texture()
        self.counter += 1
        self.counter %= len(self.textures)

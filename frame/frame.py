import pygame
from threads.thread import Thread
from frame.world import World
from objects.widgets.label import Label
from physics.coordinates import Coordinates
from frame.settings import Settings
from objects.images.animation_library import AnimationLibrary


class Frame(object):
    coordinates = Coordinates(0, 0)
    default_coordinates = Coordinates(0, 0)
    max_fps = 1000
    scale = Coordinates(1, 1)
    flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    screen = None

    def __init__(self):
        Frame.scale = Settings.frame_dimensions / Coordinates(800, 600)
        pygame.init()
        logo = pygame.image.load('resources/frame_kit/logo.png')
        pygame.event.set_grab(Settings.mouse_confined)
        pygame.display.set_icon(logo)
        pygame.display.set_caption('Game')
        Frame.screen = pygame.display.set_mode(Settings.frame_dimensions.get(), Frame.flags)
        self.fps_clock = pygame.time.Clock()
        self.fps_counter = Label('0', 30, (0, 255, 0))
        self.thread = Thread(self.run, (), 'frame')

    def run(self):
        for game_object in World.get_display():
            c = game_object.get_coordinates()
            scale = Frame.scale
            if 'fixed' not in game_object.type:
                c += Frame.default_coordinates
                c *= Settings.frame_additional_scale
            for animation in game_object.animations:
                self.blit(animation.get_texture(), c + animation.get_coordinates(), scale)
            for text in game_object.texts:
                self.blit(text.get_texture(), c + text.get_coordinates(), scale)
        self.fps_counter.set_text(str(int(self.fps_clock.get_fps())))
        self.blit(self.fps_counter.get_texture(), Coordinates(10, 0), Frame.scale)
        self.fps_clock.tick(Frame.max_fps)
        try:
            pygame.display.update()
        except pygame.error:
            pass

    def resize(self, w, h):
        size = Coordinates(w, h)
        Settings.frame_dimensions = size
        Frame.screen = None
        Frame.screen = pygame.display.set_mode(Settings.frame_dimensions.get(), Frame.flags)
        Frame.scale = Settings.frame_dimensions / Coordinates(800, 600)

    def blit(self, texture, coordinates, scale):
        if texture is not None and self.screen is not None:
            try:
                if abs(coordinates) < 10000:
                    self.screen.blit(texture, (coordinates * scale).get())
            except pygame.error:  # raises when images are still loading
                pass

    '''@staticmethod
    def update_screen():
        Frame.scale = Settings.frame_dimensions / Coordinates(800, 600)'''

    def get_scale(self):
        return Frame.scale

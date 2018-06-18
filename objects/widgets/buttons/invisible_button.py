from objects.widgets.button import Button
from objects.widgets.label import Label
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from frame.world import World
from frame.settings import Settings


class InvisibleButton(Button):

    def __init__(self, coordinates, click_function, width, height):
        self.click_function = click_function
        Button.__init__(self, [StaticAnimation(self, 'resources\\test_images\\invisible.png')], [])
        self.width = width
        self.height = height
        self.coordinates = coordinates

    def __repr__(self):
        return str(self.coordinates) + ' ' + str(self.click_function)

    def click(self):
        self.click_function()

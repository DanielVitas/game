from objects.widgets.button import Button
from objects.widgets.label import Label
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from frame.world import World
from frame.settings import Settings


class MenuTextButton(Button):

    def __init__(self, text, size, text_coordinates, coordinates, click_function, scale=Coordinates(1, 1)):
        lab = Label(text, size)
        lab.coordinates = text_coordinates
        self.click_function = click_function
        Button.__init__(self, [StaticAnimation(self, 'resources\\test_images\\menu_text_button.png')], [lab])
        self.width = 100
        self.height = 50
        self.change_scale(scale)
        self.coordinates = coordinates

    def __repr__(self):
        return str(self.coordinates) + ' ' + str(self.click_function)

    def click(self):
        self.click_function()

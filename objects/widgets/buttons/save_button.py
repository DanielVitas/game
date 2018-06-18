from objects.widgets.button import Button
from objects.widgets.label import Label
from objects.images.static_animation import StaticAnimation
from physics.coordinates import Coordinates
from frame.world import World
from frame.settings import Settings


class SaveButton(Button):

    def __init__(self):
        save = Label('SAVE', 30)
        save.coordinates = Coordinates(23, 17)
        Button.__init__(self, [StaticAnimation(self, 'resources\\test_images\\start_button_background.png')], [save])
        self.width = 100
        self.height = 50

    def click(self):
        World.write()

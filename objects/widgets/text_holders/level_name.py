from objects.widgets.label import Label
from objects.widgets.text_holder import TextHolder
from physics.coordinates import Coordinates


class LevelName(TextHolder):

    def __init__(self, text, size, coordinates):
        lab = Label(text, size)
        lab.coordinates = Coordinates(0, 0)
        TextHolder.__init__(self, [], [lab])
        self.coordinates = coordinates

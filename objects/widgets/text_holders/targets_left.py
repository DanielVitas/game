from objects.widgets.label import Label
from objects.widgets.text_holder import TextHolder
from physics.coordinates import Coordinates


class TargetsLeft(TextHolder):

    def __init__(self):
        lab = Label('', 30, (255, 0, 0))
        lab.coordinates = Coordinates(0, 0)
        TextHolder.__init__(self, [], [lab])
        self.coordinates = Coordinates(635, 10)
        self.base_text = 'Targets left: '

    def update(self, number):
        self.texts[0].set_text(self.base_text + str(number))

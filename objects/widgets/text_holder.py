from objects.widgets.widget import Widget


class TextHolder(Widget):

    def __init__(self, animations, texts):
        Widget.__init__(self, animations)
        self.texts = texts
        self.type += ['unmovable']

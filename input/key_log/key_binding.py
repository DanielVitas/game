class KeyBinding(object):

    def __init__(self, name, key=None):
        self.name = name
        self.key = key

    def check(self):
        return self.key.check()

class AnimationLibrary(object):
    animations = list()
    frame = None

    def __init__(self, frame):
        AnimationLibrary.frame = frame

    @staticmethod
    def add(animation):
        AnimationLibrary.animations.append(animation)

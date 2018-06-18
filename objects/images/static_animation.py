from objects.images.animation import Animation
from objects.images.object_image import ObjectImage
from physics.coordinates import Coordinates


class StaticAnimation(Animation):

    def __init__(self, obj, path, scale=Coordinates(1, 1), coordinates=Coordinates(0, 0), name='static animation'):
        Animation.__init__(self, obj, [ObjectImage(path, coordinates, scale)], [-1], name)

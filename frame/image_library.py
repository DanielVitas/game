import os
from frame.image import Image
from physics.coordinates import Coordinates


class ImageLibrary(object):
    default_path = 'resources\\test_images'
    images = dict()

    @staticmethod
    def __init__():
        for path in ImageLibrary.get_all_file_paths():
            ImageLibrary.add_to_images(path)
        with open('files\\image_scales.txt') as f:
            for line in f:
                line = line.split('; ')
                ImageLibrary.get_image(line[2].replace('\n', '')).scale = Coordinates(int(line[0]), int(line[1]))

    @staticmethod
    def get_all_file_paths(path=default_path):
        path_list = list()
        for p in os.walk(path):
            for file in p[2]:
                path_list.append(p[0] + '\\' + file)
        return path_list

    @staticmethod
    def add_to_images(path):
        ImageLibrary.images[path] = Image(path)

    @staticmethod
    def get_image(path):
        return ImageLibrary.images[path]

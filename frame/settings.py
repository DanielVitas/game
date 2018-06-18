import pygame

from physics.coordinates import Coordinates


class Settings(object):
    path = 'user_settings\\general_settings.txt'
    frame_dimensions = Coordinates(800, 600)
    frame_additional_scale = Coordinates(1, 1)
    main_character_name = 'Kirito'
    mouse_confined = False

    def __init__(self):
        Settings.load_settings()

    @staticmethod
    def settings(a):
        if a[0] == 'frame_dimensions':
            Settings.frame_dimensions = Coordinates(int(a[1]), int(a[2]))
        if a[0] == 'frame_additional_scale':
            Settings.frame_additional_scale = Coordinates(float(a[1]), float(a[2]))
        if a[0] == 'main_character_name':
            Settings.main_character_name = a[1].replace('\n', '')
        if a[0] == 'mouse_confined':
            if a[1] == 'True\n':
                Settings.mouse_confined = True
            else:
                Settings.mouse_confined = False

    @staticmethod
    def write_settings():
        with open(Settings.path, 'w') as file:
            file.write('frame_dimensions; ' + str(Settings.frame_dimensions.x) + '; ' +
                       str(Settings.frame_dimensions.y) + '\n')
            file.write('frame_additional_scale; ' + str(Settings.frame_additional_scale.x) + '; ' +
                       str(Settings.frame_additional_scale.y) + '\n')
            file.write('main_character_name; ' + Settings.main_character_name + '\n')
            file.write('mouse_confined; ' + str(Settings.mouse_confined) + '\n')

    @staticmethod
    def load_settings():
        with open(Settings.path, 'r') as file:
            for line in file:
                a = line.split('; ')
                Settings.settings(a)

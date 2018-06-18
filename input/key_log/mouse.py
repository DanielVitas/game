from frame.settings import Settings
from physics.coordinates import Coordinates
from input.key_log.key import Key
from frame.frame import Frame
from frame.world import World


class Mouse(object):
    buttons = {1: Key(1, 'MOUSE1'), 2: Key(2, 'MOUSE2'), 3: Key(3, 'MOUSE3'), 4: Key(4, 'BAD'), 5: Key(5, 'BAD')}
    coordinates = Coordinates(0, 0)
    selected = None

    def __int__(self, position=Coordinates(0, 0)):
        Mouse.coordinates = position

    @staticmethod
    def hover():
        for world in World.get_selectable():
            for obj in world:
                if Mouse.hovering(obj):
                    return obj
        return None

    @staticmethod
    def hovering(obj):
        coordinates = Mouse.coordinates
        if 'fixed' not in obj.type:
            coordinates -= Frame.default_coordinates
        else:
            coordinates *= Settings.frame_additional_scale
        c = obj.get_coordinates()
        if coordinates.x < c.x:
            return False
        if coordinates.x > c.x + obj.get_width():
            return False
        if coordinates.y < c.y:
            return False
        if coordinates.y > c.y + obj.get_height():
            return False
        return True

    @staticmethod
    def select(obj):
        if obj is not None:
            if 'selected' not in obj.type:
                obj.type.append('selected')
            Mouse.selected = obj
            if 'button' in obj.type:
                obj.click()

    @staticmethod
    def deselect():
        if Mouse.selected is not None:
            if 'selected' in Mouse.selected.type:
                Mouse.selected.type.remove('selected')
            Mouse.selected = None

    @staticmethod
    def reposition(new_position):
        v = (Coordinates(new_position[0], new_position[1]) / Frame.scale - Mouse.get_coordinates()) / Settings.\
            frame_additional_scale
        Mouse.coordinates = (Coordinates(new_position[0], new_position[1]) / Frame.scale) / Settings.\
            frame_additional_scale
        if Mouse.selected is not None:
            if not [x for x in ['fixed', 'unmovable'] if x in Mouse.selected.type]:
                Mouse.selected.reposition(Mouse.selected.get_coordinates() + v)

    @staticmethod
    def button_press(button):
        Mouse.buttons[button].press()

    @staticmethod
    def button_release(button):
        Mouse.buttons[button].release()

    @staticmethod
    def check(button):
        return Mouse.buttons[button].check()

    @staticmethod
    def get_coordinates():
        return Mouse.coordinates * Settings.frame_additional_scale

    @staticmethod
    def get_real_coordinates():
        return Mouse.coordinates - Frame.default_coordinates

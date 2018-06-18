from frame.settings import Settings
from physics.coordinates import Coordinates
from frame.frame import Frame
from input.key_log.mouse import Mouse


class Borders(object):
    coordinates = Coordinates(50, 50)
    a = 700
    b = 500
    focus_object = None
    mouse_speed = Coordinates(10, 10)

    def __init__(self):
        pass

    @staticmethod
    def lock():
        Borders.a = 100
        Borders.b = 100
        Borders.coordinates = Coordinates(350, 250)

    @staticmethod
    def unlock():
        Borders.a = 700
        Borders.b = 500
        Borders.coordinates = Coordinates(50, 50)

    @staticmethod
    def in_borders(coordinates):
        a = True
        v = []
        c = coordinates
        if c.x < Borders.coordinates.x:
            a = False
            v.append(Coordinates(1, 0))
        if c.x > Borders.coordinates.x + Borders.a:
            a = False
            v.append(Coordinates(-1, 0))
        if c.y < Borders.coordinates.y:
            a = False
            v.append(Coordinates(0, 1))
        if c.y > Borders.coordinates.y + Borders.b:
            a = False
            v.append(Coordinates(0, -1))
        return a, v

    @staticmethod
    def focus():
        v = Coordinates(0, 0)
        if Borders.focus_object is None:
            v += Borders.focus_mouse()
        if Borders.focus_object is not None:
            if Borders.focus_object.width * Settings.frame_additional_scale.x < Borders.a and\
                    Borders.focus_object.height * Settings.frame_additional_scale.y < Borders.b:
                v += Borders.focus_obj()
        if Mouse.selected is not None:
            if 'fixed' not in Mouse.selected.type:
                Mouse.selected.reposition(Mouse.selected.get_coordinates() - v)

    @staticmethod
    def focus_obj():
        c = Borders.focus_object
        v = Coordinates(Frame.default_coordinates.x, Frame.default_coordinates.y)
        if c.get_coordinates().x + Frame.default_coordinates.x < Borders.coordinates.x / Settings.\
                frame_additional_scale.x:
            v.x -= Borders.coordinates.x / Settings.frame_additional_scale.x - c.get_coordinates().x
            Frame.default_coordinates.x = Borders.coordinates.x / Settings.frame_additional_scale.x\
                                          - c.get_coordinates().x
        elif c.get_coordinates().x + c.get_width() + Frame.default_coordinates.x > (Borders.coordinates.x + Borders.a)\
                / Settings.frame_additional_scale.x:
            v.x -= (Borders.coordinates.x + Borders.a) / Settings.frame_additional_scale.x - c.get_coordinates().x\
                   - c.get_width()
            Frame.default_coordinates.x = (Borders.coordinates.x + Borders.a) / Settings.frame_additional_scale.x\
                                          - c.get_coordinates().x - c.get_width()
        else:
            v.x = 0
        if c.get_coordinates().y + Frame.default_coordinates.y < Borders.coordinates.y\
                / Settings.frame_additional_scale.x:
            v.y -= Borders.coordinates.y / Settings.frame_additional_scale.x - c.get_coordinates().y
            Frame.default_coordinates.y = Borders.coordinates.y / Settings.frame_additional_scale.x\
                                          - c.get_coordinates().y
        elif c.get_coordinates().y + c.get_height() + Frame.default_coordinates.y > (Borders.coordinates.y + Borders.b)\
                / Settings.frame_additional_scale.x:
            v.y -= (Borders.coordinates.y + Borders.b) / Settings.frame_additional_scale.x - c.get_coordinates().y\
                   - c.get_height()
            Frame.default_coordinates.y = (Borders.coordinates.y + Borders.b) / Settings.frame_additional_scale.x\
                                          - c.get_coordinates().y - c.get_height()
        else:
            v.y = 0
        return v * (-1)

    @staticmethod
    def focus_mouse():
        b = Borders.in_borders(Mouse.get_coordinates())
        v = Coordinates(0, 0)
        if not b[0]:
            for i in b[1]:
                Frame.default_coordinates += Borders.mouse_speed / Settings.frame_additional_scale * i
                v += Borders.mouse_speed / Settings.frame_additional_scale * i
        return v


    @staticmethod
    def gain_focus(focus_object):
        Borders.lose_focus()
        Borders.focus_object = focus_object

    @staticmethod
    def lose_focus():
        Borders.focus_object = None

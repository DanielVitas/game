from bisect import bisect


class World(object):
    display = list()
    values = list()
    hittable = list()
    writable = list()
    gravity_fields = list()
    buttons = list()
    main_character = None
    level = None
    paused_display = list()
    paused_values = list()

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def add(obj):
        if 'gravity field' in obj.type:
            World.gravity_fields.append(obj)
        elif 'hittable' in obj.type:
            World.hittable.append(obj)
        elif 'button' in obj.type:
            World.buttons.append(obj)
        if 'writable' in obj.type:
            World.writable.append(obj)
        World.add_display(obj)

    @staticmethod
    def remove(obj):
        try:
            if 'gravity field' in obj.type:
                World.gravity_fields.remove(obj)
            elif 'hittable' in obj.type:
                World.hittable.remove(obj)
            elif 'button' in obj.type:
                World.buttons.remove(obj)
            if 'writable' in obj.type:
                World.writable.remove(obj)
            World.remove_display(obj)
        except ValueError:
            pass

    @staticmethod
    def promote_main(main_char):
        World.demote_main()
        World.main_character = main_char

    @staticmethod
    def demote_main():
        World.main_character = None

    @staticmethod
    def add_display(obj):
        priority = obj.priority
        i = bisect(World.values, priority)
        World.values.insert(i, priority)
        World.display.insert(i, obj)

    @staticmethod
    def remove_display(obj):
        World.display.remove(obj)
        World.values.remove(obj.priority)

    @staticmethod
    def get_display():
        return World.display

    @staticmethod
    def setup_level(level):
        World.level = level
        level.load()

    @staticmethod
    def write(path=None, level=None):
        if level is None:
            level = World.level
        if path is None:
            level.write()
        else:
            level.write(path)

    @staticmethod
    def clear_level():
        World.full_clear()
        World.level = None

    @staticmethod
    def full_clear():
        World.display = []
        World.values = []
        World.hittable = []
        World.writable = []
        World.gravity_fields = []
        World.buttons = []
        World.paused_display = []
        World.paused_values = []
        World.main_character = None

    @staticmethod
    def pause():
        World.paused_display = World.display
        World.paused_values = World.values

    @staticmethod
    def resume():
        World.display = World.paused_display
        World.values = World.paused_values

    @staticmethod
    def clear_display():
        World.display = list()
        World.values = list()

    @staticmethod
    def get_selectable():
        return [World.buttons, World.gravity_fields, World.writable]

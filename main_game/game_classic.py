from frame.frame import Frame
from frame.settings import Settings
from input.key_log.key_logger import KeyLogger
from input.key_log.mouse import Mouse
from main_game.game_builder import GameBuilder
from objects.game_object.dinamic.shoot_marker import ShootMarker
from physics.coordinates import Coordinates
from physics.vector import Vector
from frame.world import World
from main_game.game_state import GameState
from objects.game_object.dinamic.gravity_fields.normal_gravity_field import NormalGravityField
from frame.borders import Borders
from thread_lock import target_fps


class GameClassic(GameState):

    def __init__(self, game_states):
        GameState.__init__(self)
        self.game_states = game_states
        self.add(self.move, 1 / target_fps)
        self.add(self.delete_gf, 1/10)
        self.add(self.shoot, 1 / 2)
        self.add(self.create_gravity_field, 1/2)
        self.add(self.back, 1 / 20)
        self.add(self.zoom_out, 1 / target_fps)
        self.add(self.zoom_in, 1 / target_fps)
        self.add(self.recenter, 1 / 3)
        self.add(self.change_perspective, 1 / 1)
        self.word_to_vector = {'up': Vector(0, -1), 'down': Vector(0, 1), 'left': Vector(-1, 0), 'right': Vector(1, 0)}

    def move(self):
        if World.main_character is not None:
            for word in ['up', 'down', 'left', 'right']:
                if KeyLogger.bindings[word].check():
                    World.main_character.move(self.word_to_vector[word])
            Borders.focus()
        return True

    def recenter(self):
        if KeyLogger.bindings['recenter'].check():
            if World.main_character is not None:
                print(World.main_character.get_coordinates())
                Frame.default_coordinates = Coordinates(375, 275) / Settings.frame_additional_scale -\
                                            World.main_character.get_coordinates()
            return True
        return False

    def change_perspective(self):
        if KeyLogger.bindings['perspective'].check():
            if Borders.focus_object is None:
                Borders.gain_focus(World.main_character)
                Borders.lock()
            else:
                Borders.lose_focus()
                Borders.unlock()
            return True
        return False

    def zoom_out(self):
        if KeyLogger.bindings['zoomout'].check():
            Settings.frame_additional_scale *= Coordinates(1, 1) / (Coordinates(1, 1) +
                                                                    GameBuilder.zoomin_scale / target_fps)
            return True
        return False

    def zoom_in(self):
        if KeyLogger.bindings['zoomin'].check():
            Settings.frame_additional_scale *= Coordinates(1, 1) + GameBuilder.zoomin_scale / target_fps
            return True
        return False

    def delete_gf(self):
        if KeyLogger.bindings['delete'].check():
            self.select_gf()
            if Mouse.selected is not None:
                if 'gravity field' in Mouse.selected.type and 'spawn' not in Mouse.selected.type:
                    print('Deleted:', Mouse.selected.__class__.__name__)
                    Mouse.selected.world_remove()
                    Mouse.deselect()
            return True
        return False

    def select_gf(self):
        if Mouse.selected is None:
            a = Mouse.hover()
            if a is not None:
                if 'gravity field' in a.type:
                    Mouse.selected = a
        else:
            if 'gravity field' not in Mouse.selected.type:
                a = Mouse.hover()
                if a is not None:
                    if 'gravity field' in a.type:
                        Mouse.selected = a

    def shoot(self):
        if World.main_character is not None:
            if KeyLogger.bindings['shoot'].check():
                v = Vector(Mouse.get_real_coordinates() - World.main_character.get_firing_coordinates())
                World.main_character.fire_normal_bullet(v.normalize())
                return True
        return False

    def create_gravity_field(self):
        if World.main_character is not None:
            if KeyLogger.bindings['gravity'].check():
                gf = NormalGravityField()
                gf.coordinates = Mouse.get_real_coordinates() - Coordinates(gf.width / 2, gf.height / 2)
                gf.type.append('unmovable')
                World.add(gf)
                return True
        return False

    def back(self):
        if KeyLogger.bindings['escape'].check():
            self.game_states.change_submenu(9)
            return True
        return False

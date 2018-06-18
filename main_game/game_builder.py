from frame.frame import Frame
from input.key_log.key_logger import KeyLogger
from input.key_log.mouse import Mouse
from objects.game_object.dinamic.obstacles.blocks.shootable_block import ShootableBlock
from objects.game_object.dinamic.obstacles.blocks.walkable_block import WalkableBlock
from physics.vector import Vector
from frame.world import World
from main_game.game_state import GameState
from objects.game_object.dinamic.gravity_fields.normal_gravity_field import NormalGravityField
from frame.borders import Borders
from objects.game_object.dinamic.obstacles.blocks.grey_block import GreyBlock
from objects.game_object.dinamic.obstacles.targets.classic_target import ClassicTarget
from objects.game_object.dinamic.spawn import Spawn
from physics.coordinates import Coordinates
from frame.settings import Settings
from thread_lock import target_fps


class GameBuilder(GameState):
    zoomin_scale = Coordinates(0.8, 0.8)
    stretch_addon = Coordinates(3.0, 3.0)

    def __init__(self, game_states):
        GameState.__init__(self)
        self.game_states = game_states
        self.add(self.move, 1 / target_fps)
        self.add(self.shoot, 1 / 2)
        self.add(self.create_gravity_field, 1 / 3)
        self.add(self.create_block, 1 / 5)
        self.add(self.create_shootable_block, 1 / 5)
        self.add(self.create_target, 1 / 5)
        self.add(self.create_spawn, 1 / 5)
        self.add(self.select_object, 1 / target_fps)
        self.add(self.delete_object, 1 / 10)
        self.add(self.change_perspective, 1 / 1)
        self.add(self.zoom_out, 1 / target_fps)
        self.add(self.zoom_in, 1 / target_fps)
        self.add(self.stretch_up, 1 / target_fps)
        self.add(self.stretch_down, 1 / target_fps)
        self.add(self.stretch_left, 1 / target_fps)
        self.add(self.stretch_right, 1 / target_fps)
        self.add(self.recenter, 1 / 3)
        self.add(self.back, 1 / 20)
        self.word_to_vector = {'up': Vector(0, -1), 'down': Vector(0, 1), 'left': Vector(-1, 0), 'right': Vector(1, 0)}

    def recenter(self):
        if KeyLogger.bindings['recenter'].check():
            if World.main_character is not None:
                f = Coordinates(375, 275) / Settings.frame_additional_scale -\
                                            World.main_character.get_coordinates()
                v = f - Frame.default_coordinates
                if Mouse.selected is not None:
                    if 'fixed' not in Mouse.selected.type:
                        Mouse.selected.reposition(Mouse.selected.get_coordinates() - v)
                Frame.default_coordinates = f
            return True
        return False

    def create_block(self):
        if KeyLogger.bindings['spawn1'].check():
            block = GreyBlock(50, 50)
            block.coordinates = Mouse.get_real_coordinates() - Coordinates(block.width / 2, block.height / 2)
            World.add(block)
            return True
        return False

    def create_target(self):
        if KeyLogger.bindings['spawn3'].check():
            target = ClassicTarget()
            target.coordinates = Mouse.get_real_coordinates() - Coordinates(target.width / 2, target.height / 2)
            World.add(target)
            return True
        return False

    def create_shootable_block(self):
        if KeyLogger.bindings['spawn2'].check():
            sblock = ShootableBlock(50, 50)
            sblock.coordinates = Mouse.get_real_coordinates() - Coordinates(sblock.width / 2, sblock.height / 2)
            World.add(sblock)
            return True
        return False

    def create_spawn(self):
        if KeyLogger.bindings['spawn4'].check():
            if World.level.spawn is not None:
                World.remove(World.level.spawn)
            spawn = Spawn()
            spawn.coordinates = Mouse.get_real_coordinates() - Coordinates(spawn.width / 2, spawn.height / 2)
            World.level.spawn = spawn
            World.add(spawn)
            return True
        return False

    def select_object(self):
        if KeyLogger.bindings['shoot'].check():
            if Mouse.selected is None:
                Mouse.select(Mouse.hover())
        else:
            Mouse.deselect()
            return True
        return False

    def delete_object(self):
        if KeyLogger.bindings['delete'].check():
            if Mouse.selected is not None:
                if 'spawn' not in Mouse.selected.type:
                    print('Deleted:', Mouse.selected.__class__.__name__)
                    Mouse.selected.world_remove()
                    Mouse.deselect()
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

    def stretch_up(self):
        if KeyLogger.bindings['arrowup'].check():
            if Mouse.selected is not None:
                if 'block' in Mouse.selected.type or 'target' in Mouse.selected.type:
                    Mouse.selected.add_scale(Coordinates(0, -GameBuilder.stretch_addon.y) / target_fps)
            return True
        return False

    def stretch_down(self):
        if KeyLogger.bindings['arrowdown'].check():
            if Mouse.selected is not None:
                if 'block' in Mouse.selected.type or 'target' in Mouse.selected.type:
                    Mouse.selected.add_scale(Coordinates(0, GameBuilder.stretch_addon.y) / target_fps)
            return True
        return False

    def stretch_left(self):
        if KeyLogger.bindings['arrowleft'].check():
            if Mouse.selected is not None:
                if 'block' in Mouse.selected.type or 'target' in Mouse.selected.type:
                    Mouse.selected.add_scale(Coordinates(-GameBuilder.stretch_addon.x, 0) / target_fps)
            return True
        return False

    def stretch_right(self):
        if KeyLogger.bindings['arrowright'].check():
            if Mouse.selected is not None:
                if 'block' in Mouse.selected.type or 'target' in Mouse.selected.type:
                    Mouse.selected.add_scale(Coordinates(GameBuilder.stretch_addon.x, 0) / target_fps)
            return True
        return False

    def move(self):
        if World.main_character is not None:
            for word in ['up', 'down', 'left', 'right']:
                if KeyLogger.bindings[word].check():
                    World.main_character.move(self.word_to_vector[word])
            Borders.focus()
        return True

    def shoot(self):
        if World.main_character is not None:
            if KeyLogger.bindings['select'].check():
                v = Vector(Mouse.get_real_coordinates() - World.main_character.get_firing_coordinates())
                World.main_character.fire_normal_bullet(v.normalize())
                return True
        return False

    def create_gravity_field(self):
        if World.main_character is not None:
            if KeyLogger.bindings['gravity'].check():
                gf = NormalGravityField()
                gf.coordinates = Mouse.get_real_coordinates() - Coordinates(gf.width / 2, gf.height / 2)
                World.add(gf)
                return True
        return False

    def back(self):
        if KeyLogger.bindings['escape'].check():
            self.game_states.change_submenu(3)
            return True
        return False

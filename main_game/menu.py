import pygame

import thread_lock
from frame.world import World
from input.key_log.key_logger import KeyLogger
from input.key_log.mouse import Mouse
from main_game.game_state import GameState


class Menu(GameState):

    def __init__(self, gamestates, number, back_number):
        GameState.__init__(self)
        self.gamestates = gamestates
        self.number = number
        self.back_number = back_number
        self.world = []
        self.add(self.escape, 1 / 20)
        self.add(self.select, 1 / thread_lock.target_fps)

    def change_to(self, submenu):
        self.gamestates.change_submenu(submenu)

    def add_list(self, arr):
        for obj in arr:
            self.world.append(obj)

    def load(self):
        for obj in self.world:
            World.add(obj)

    def empty(self):
        for obj in self.world:
            obj.world_remove()

    def back(self):
        if self.back_number == 0:
            event = pygame.event.Event(pygame.QUIT, {})
            pygame.event.post(event)
        elif self.back_number == 1:
            thread_lock.pause_main = False
            World.resume()
            self.gamestates.state = self.gamestates.BUILDER
            self.empty()
            self.gamestates.sleep()
        elif self.back_number == 2:
            thread_lock.pause_main = False
            World.resume()
            self.gamestates.state = self.gamestates.GAME
            self.empty()
            self.gamestates.sleep()
        else:
            self.change_to(self.back_number)

    def escape(self):
        if KeyLogger.bindings['escape'].check():
            self.back()
            return True
        return False

    def select(self):
        if KeyLogger.bindings['shoot'].check():
            if Mouse.selected is None:
                a = Mouse.hover()
                if a is not None:
                    if 'button' in a.type:
                        Mouse.select(a)
        else:
            Mouse.deselect()
            return True
        return False

    def begin(self):
        pass

    def end(self):
        pass

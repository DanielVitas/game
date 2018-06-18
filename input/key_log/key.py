import time
from thread_lock import target_fps


class Key(object):

    def __init__(self, key_id, name=None):
        self.base_cooldown = 1 / target_fps
        self.key_id = key_id
        self.name = name
        self.pressed = False
        self.last_check = 0

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False

    def check(self):
        if self.pressed:
            if time.time() - self.last_check > self.base_cooldown:
                self.last_check = time.time()
                return True
        return False

    def get_name(self):
        if self.name is None:
            return str(self.key_id)
        else:
            return self.name

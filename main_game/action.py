import time


class Action(object):

    def __init__(self, fun, args,  cooldown, condition):
        self.fun = fun
        self.args = args
        self.cooldown = cooldown
        self.last_check = 0
        self.condition = condition

    def run(self):
        if self.condition():
            if time.time() - self.last_check > self.cooldown:
                if self.args != ():
                    a = self.fun(self.args)
                else:
                    a = self.fun()
                if a:
                    self.last_check = time.time()

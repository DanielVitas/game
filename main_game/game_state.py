from main_game.action import Action


class GameState(object):

    def __init__(self):
        self.actions = list()

    def run(self):
        for action in self.actions:
            action.run()

    def add(self, fun, cooldown, condition=None, args=()):
        if condition is None:
            condition = self.default_condition  #(lambda: True)
        action = Action(fun, args, cooldown, condition)
        self.actions.append(action)

    def default_condition(self):
        return True

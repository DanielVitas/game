import os


class MenuLibrary(object):
    default_path = 'main_game\\menus'

    def __init__(self, game_states):
        self.menus = dict()
        menu_names = self.get_all_file_names(MenuLibrary.default_path)
        for menu in menu_names:
            m1 = menu[:-3]
            m2 = menu[0].upper() + menu[1:-3]
            exec('from main_game.menus.%s import %s' % (m1, m2))
            a = m2.split('_')
            my_menu = eval('%s(game_states)' % m2)
            self.menus[int(a[1])] = my_menu

    def get_all_file_names(self, path):
            path_list = list()
            for p in os.walk(path):
                for file in p[2]:
                    if file[-3:] != 'pyc':
                        path_list.append(file)
            return path_list

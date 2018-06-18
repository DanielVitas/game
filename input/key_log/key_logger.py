import input.key_log.key_binding as key_binding, input.key_log.key as key
from input.key_log.mouse import Mouse


class KeyLogger(object):
    bindings = dict()
    keys = dict()
    names = dict()

    @staticmethod
    def __init__():
        KeyLogger.names = {8: 'BACKSPACE',
                           9: 'TAB',
                           19: 'PAUSEBREAK',
                           13: 'ENTER',
                           27: 'ESC',
                           32: 'SPACEBAR',
                           39: '\'',
                           44: ',',
                           45: '-',
                           46: '.',
                           47: '/',
                           48: '0',
                           49: '1',
                           50: '2',
                           51: '3',
                           52: '4',
                           53: '5',
                           54: '6',
                           55: '7',
                           56: '8',
                           57: '9',
                           59: ';',
                           61: '=',
                           91: '[',
                           92: '\\',
                           93: ']',
                           96: '`',
                           97: 'A',
                           98: 'B',
                           99: 'C',
                           100: 'D',
                           101: 'E',
                           102: 'F',
                           103: 'G',
                           104: 'H',
                           105: 'I',
                           106: 'J',
                           107: 'K',
                           108: 'L',
                           109: 'M',
                           110: 'N',
                           111: 'O',
                           112: 'P',
                           113: 'Q',
                           114: 'R',
                           115: 'S',
                           116: 'T',
                           117: 'U',
                           118: 'V',
                           119: 'W',
                           120: 'X',
                           121: 'Y',
                           122: 'Z',
                           127: 'DEL',
                           273: 'UP',
                           274: 'DOWN',
                           275: 'RIGHT',
                           276: 'LEFT',
                           278: 'HOME',
                           279: 'END',
                           280: 'PAGEUP',
                           281: 'PAGEDOWN',
                           282: 'F1',
                           283: 'F2',
                           284: 'F3',
                           285: 'F4',
                           286: 'F5',
                           287: 'F6',
                           288: 'F7',
                           289: 'F8',
                           290: 'F9',
                           291: 'F10',
                           292: 'F11',
                           293: 'F12',
                           301: 'CAPS LOCK',
                           302: 'SCRLLOCK',
                           303: 'RSHIFT',
                           304: 'LSHIFT',
                           305: 'RCTRL',
                           306: 'LCTRL',
                           307: 'RALT',
                           308: 'LALT',
                           316: 'PRTSCR',
                           319: 'SCRL'}
        KeyLogger.load_keys()
        KeyLogger.load_bindings()

    @staticmethod
    def key_press(key_id, mod):
        try:
            KeyLogger.keys[key_id].press()
        except KeyError:
            print('index', key_id, 'not defined')
#w        print('press', key_id, mod)

    @staticmethod
    def key_release(key_id, mod):
        try:
            KeyLogger.keys[key_id].release()
        except KeyError:
            print('index', key_id, 'not defined')
#        print('release', key_id, mod)

    @staticmethod
    def load_bindings(path='user_settings/key_bindings.txt'):
        with open(path) as text:
            for line in text:
                a = line.split(' ')
                if int(a[1]) >= 0:
                    KeyLogger.bindings[a[0]] = key_binding.KeyBinding(a[0], KeyLogger.keys[int(a[1])])
                else:
                    KeyLogger.bindings[a[0]] = key_binding.KeyBinding(a[0], Mouse.buttons[-int(a[1])])

    @staticmethod
    def write_bindings(path='user_settings/key_bindings.txt'):
        with open(path, 'w') as text:
            for binding in KeyLogger.bindings.values():
                if binding.key in Mouse.buttons.values():
                    num = -binding.key.key_id
                else:
                    num = binding.key.key_id
                text.write('%s %s\n' % (binding.name, str(num)))

    @staticmethod
    def load_keys():
        for i in range(400):
            try:
                name = KeyLogger.names[i]
            except KeyError:
                name = None
            KeyLogger.keys[i] = key.Key(i, name)

    @staticmethod
    def rebind(name, key_id):
        KeyLogger.bindings[name].key_id = key_id

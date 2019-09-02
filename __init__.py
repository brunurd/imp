import sys
import unicodedata
from PIL import Image


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def get_arg(index, name, valids=None):
    if len(sys.argv) <= index:
        raise Exception(f'No {name} found.')

    if valids != None:
        if sys.argv[index] not in valids:
            raise Exception(f'The {name} "{sys.argv[index]}" is invalid.')

    return sys.argv[index]


def get_flag(flag_name):
    for arg in sys.argv:
        if arg == f'--{flag_name}':
            index = sys.argv.index(arg, 0, len(sys.argv)) + 1
            if len(sys.argv) > index:
                return sys.argv[index]
    return None


command = get_arg(1, 'command', ['´resize', 'trim'])
path = get_arg(2, 'path')


def resize(_path, width, height):
    pass


def trim(_path):
    image = Image.open(_path)
    width, height = image.size
    bounds = {'top': 0, 'bottom': 0, 'left': width, 'right': 0}

    for y in range(1, height):
        for x in range(1, width):
            pixel = image.getpixel((x, y))
            if pixel[3] == 0:
                continue
            elif x < bounds['left']:
                bounds['left'] = x

    print(bounds)


if command == 'resize':
    resize(path, get_flag('width'), get_flag('height'))
elif command == 'trim':
    trim(path)

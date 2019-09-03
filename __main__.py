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


def resize(_path, width, height):
    if width == None or height == None:
        raise Exception(f'--width or --height flag not set.')

    if not is_number(width) or not is_number(height):
        raise Exception(f'width or height is not a number!')

    size = (int(width), int(height))
    image = Image.open(_path)
    resized_image = image.resize(size, Image.ANTIALIAS)
    resized_image.save(_path, 'PNG')


def crop(_path, bounds):
    image = Image.open(_path)
    cropped_image = image.crop(
        (bounds['left'], bounds['top'], bounds['right'], bounds['bottom']))
    cropped_image.save(_path, 'PNG')


def trim(_path):
    image = Image.open(_path)
    width, height = image.size
    bounds = {'top': height, 'bottom': 0, 'left': width, 'right': 0}

    for y in range(1, height):
        for x in range(1, width):
            pixel = image.getpixel((x, y))
            if pixel[3] == 0:
                continue
            else:
                if x < bounds['left']:
                    bounds['left'] = x
                if x > bounds['right']:
                    bounds['right'] = x + 1
                if y < bounds['top']:
                    bounds['top'] = y
                if y > bounds['bottom']:
                    bounds['bottom'] = y + 1

    cropped_image = image.crop(
        (bounds['left'], bounds['top'], bounds['right'], bounds['bottom']))
    cropped_image.save(_path, 'PNG')


if __name__ == '__main__':
    command = get_arg(1, 'command', ['resize', 'trim', 'crop'])
    path = get_arg(2, 'path')

    if command == 'resize':
        resize(path, get_flag('width'), get_flag('height'))

    elif command == 'crop':
        crop(path, {'top': get_flag('top'), 'bottom': get_flag(
            'bottom'), 'left': get_flag('left'), 'right': get_flag('right')})

    elif command == 'trim':
        trim(path)

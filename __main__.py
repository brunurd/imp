from src.cli import Cli
from PIL import Image


def resize(_path, width, height):
    if width == None or height == None:
        raise Exception(f'--width or --height flag not set.')

    # if not is_number(width) or not is_number(height):
    #     raise Exception(f'width or height is not a number!')

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
    cli = Cli()

    command = cli.get_arg(1, 'command', ['resize', 'trim', 'crop'])
    path = cli.get_arg(2, 'path')

    if command == 'resize':
        resize(path, cli.get_flag('width', 'w'), cli.get_flag('height', 'h'))

    elif command == 'crop':
        crop(path, {'top': cli.get_flag('top', 't'), 'bottom': cli.get_flag(
            'bottom', 'b'), 'left': cli.get_flag('left', 'l'), 'right': cli.get_flag('right', 'r')})

    elif command == 'trim':
        trim(path)

    del cli
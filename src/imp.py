import re
import os
from PIL import Image


class Imp:
    def __init__(self, path):
        self.__path = path
        self.input_image = Image.open(self.__path)
        self.output_image = Image.open(self.__path)
        self.width, self.height = self.input_image.size

    def __del__(self):
        del self.__path
        del self.input_image

    def resize(self, width, height, ext=None, out=None):
        self.width = width if width != None and \
            not isinstance(width, str) else self.width

        self.height = height if height != None and \
            not isinstance(height, str) else self.height

        new_size = (int(self.width), int(self.height))

        self.output_image = self.input_image.resize(new_size, Image.ANTIALIAS)
        self.__save(ext, out)

    def crop(self, left, top, width=None, height=None, ext=None, out=None):
        if width == None:
            width = self.width - left

        if height == None:
            height = self.height - top

        right = left + width
        bottom = top + height

        self.output_image = self.input_image.crop((left, top, right, bottom))
        self.__save(ext, out)

    def convert(self, ext=None, out=None):
        self.__save(ext, out)

    def trim(self, ext=None, out=None):
        top = self.height
        bottom = 0
        left = self.width
        right = 0

        for y in range(1, self.height):
            for x in range(1, self.width):
                pixel = self.input_image.getpixel((x, y))
                if pixel[3] == 0:
                    continue
                else:
                    if x < left:
                        left = x
                    if x > right:
                        right = x + 1
                    if y < top:
                        top = y
                    if y > bottom:
                        bottom = y + 1

        self.output_image = self.input_image.crop((left, top, right, bottom))
        self.__save(ext, out)

    def __validate_extension(self, ext):
        default_value = 'PNG'

        if ext != None and isinstance(ext, str):
            ext = ext.upper()
            if ext in ['PNG', 'PPM', 'JPEG', 'JPG', 'GIF', 'TIFF', 'BMP', 'ICO']:
                ext = 'JPEG' if ext == 'JPG' else ext

                if ext == 'JPEG':
                    self.output_image = self.output_image.convert('RGB')

                return ext

        return default_value

    def __validate_out(self, ext, out):
        regex = re.compile(r'(^(.*)(\/)(.*)(\..*?[^\/]$))|(^(.*)(\/))$|(^.*$)')
        in_matches = regex.findall(self.__path)
        default_value = os.path.join(in_matches[0][1], f'{in_matches[0][3]}.{ext.lower()}')

        if out != None and isinstance(out, str):
            out_matches = regex.findall(out)

            if len(in_matches) > 0 and len(out_matches) > 0:
                directory = out_matches[0][8] if out_matches[0][8] else ''
                directory = out_matches[0][6] if out_matches[0][6] else directory
                directory = out_matches[0][1] if out_matches[0][1] else directory
                directory = directory if directory else in_matches[0][1]
                filename = out_matches[0][3] if out_matches[0][3] else in_matches[0][3]

                if not os.path.isdir(directory):
                    os.makedirs(directory)

                return os.path.join(directory, f'{filename}.{ext.lower()}')

        return default_value


    def __save(self, ext, out):
        ext = self.__validate_extension(ext)
        out = self.__validate_out(ext, out)
        self.output_image.save(out, ext)

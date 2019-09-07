import re
import os
from PIL import Image


class Imp:
    def __init__(self, path):
        directory = os.path.dirname(path)
        filename, ext = os.path.splitext(os.path.basename(path))

        self.__directory = directory if directory else '.'
        self.__filename = filename if filename else 'image'
        self.__extension = 'PNG'

        regex = re.compile(r'^\.(.*)$')

        if regex.search(ext):
            ext = regex.findall(ext)[0].upper()
            if ext in ['PNG', 'PPM', 'JPEG', 'JPG', 'GIF', 'TIFF', 'BMP', 'ICO']:
                ext = 'JPEG' if ext == 'JPG' else ext
                self.__extension = ext

        self.__image = Image.open(path)

    def __del__(self):
        del self.__image

    def get_path(self):
        return os.path.join(self.__directory, f'{self.__filename}.{self.__extension.lower()}')

    def set_path(self, path):
        directory = os.path.dirname(path)
        filename, ext = os.path.splitext(os.path.basename(path))

        self.__directory = directory if directory else self.__directory
        self.__filename = filename if filename else self.__filename

        regex = re.compile(r'^\.(.*)$')
        if regex.search(ext):
            self.set_extension(regex.findall(ext)[0])

    def set_extension(self, ext):
        ext = ext.upper()
        if ext in ['PNG', 'PPM', 'JPEG', 'JPG', 'GIF', 'TIFF', 'BMP', 'ICO']:
            ext = 'JPEG' if ext == 'JPG' else ext
            self.__extension = ext

    def save(self, path=None):
        if path != None:
            self.set_path(path)

        if self.__extension == 'JPEG':
                self.__image = self.__image.convert('RGB')

        self.__image.save(self.get_path(), self.__extension)

    def __validate_number(self, number, fallback):
        return number if number != None and not isinstance(number, str) else fallback

    def resize(self, width, height):
        old_width, old_height = self.__image.size

        width = self.__validate_number(width, old_width)
        height = self.__validate_number(height, old_height)

        new_size = (int(width), int(height))

        self.__image = self.__image.resize(new_size, Image.ANTIALIAS)

    def crop(self, left, top, width=None, height=None):
        old_width, old_height = self.__image.size

        width = self.__validate_number(width, old_width)
        height = self.__validate_number(height, old_height)

        right = left + width
        bottom = top + height

        self.__image = self.__image.crop((left, top, right, bottom))

    def convert(self, ext=None):
        self.set_extension(ext)

    def trim(self, ext=None):
        width, height = self.__image.size
        top = height
        bottom = 0
        left = width
        right = 0

        for y in range(1, height):
            for x in range(1, width):
                pixel = self.__image.getpixel((x, y))
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

        self.__image = self.__image.crop((left, top, right, bottom))

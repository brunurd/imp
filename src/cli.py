import sys
import unicodedata


class Cli:
    __args = []

    def __init__(self):
        self.__args = sys.argv

    def __del__(self):
        del self.__args

    def __is_number(self, s):
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

    def get_arg(self, index, name, valids=None):
        if len(self.__args) <= index:
            raise Exception(f'No {name} found.')

        if valids != None:
            if self.__args[index] not in valids:
                raise Exception(
                    f'The {name} "{self.__args[index]}" is invalid.')

        arg = self.__args[index]
        return float(arg) if self.__is_number(arg) else arg

    def get_flag_value(self, flag_name, flag_shortcut=None):
        for arg in self.__args:
            if arg == f'--{flag_name}' or arg == f'-{flag_shortcut}':
                index = self.__args.index(arg, 0, len(self.__args)) + 1
                if len(self.__args) > index:
                    flag = self.__args[index]
                    return float(flag) if self.__is_number(flag) else flag
        return None

    def flag_exists(self, flag_name, flag_shortcut=None):
        for arg in self.__args:
            if arg == f'--{flag_name}' or arg == f'-{flag_shortcut}':
                return True
        return False

import colorama
from src.cli import Cli
from src.imp import Imp

def log(s):
    print(f'IMP: {str(s)}')

def error(s):
    print(f'{colorama.Fore.RED}IMP: Error: {str(s)}{colorama.Style.RESET_ALL}')

def main():
    help_text = """

Help:
    imp <command> <input-file> <optional flags>

Example: imp convert ~/image.png -ext ico

Commands:
    trim     Remove transparent pixels in the edges of the image.
    convert  Change a file image type.
    resize   Resize a image.
    crop     Crop a part of the image.

Flags:
    --width   -w   Width of the output image.
    --height  -h   Height of the output image.
    --top     -t   The top of a crop rect.
    --left    -l   The left of a crop rect.
    --ext     -e   The output extension.
    --out     -o   The output path.

"""

    colorama.init()
    try :
        cli = Cli()
        command = cli.get_arg(1, 'command', ['resize', 'trim', 'crop', 'convert', 'help'])
        path = cli.get_arg(2, 'path')
        imp = Imp(path)

        # Flags.
        w = cli.get_flag('width', 'w')
        h = cli.get_flag('height', 'h')
        t = cli.get_flag('top', 't')
        l = cli.get_flag('left', 'l')
        e = cli.get_flag('ext', 'e')
        o = cli.get_flag('out', 'o')

        if command == 'resize':
            imp.resize(w, h, e, o)
            log('Image resized with success!')

        elif command == 'crop':
            imp.crop(l, t, w, h, e, o)
            log('Image cropped with success!')

        elif command == 'trim':
            imp.trim(e, o)
            log('Image trimmed with success!')
        
        elif command == 'convert':
            imp.convert(e, o)
            log('Image converted with success!')

        elif command == 'help':
            print(help_text)

        del cli
        del imp

    except Exception as e:
        print(help_text)
        error(e)

if __name__ == '__main__':
    main()

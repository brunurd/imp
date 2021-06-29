import colorama
from src.cli import Cli
from src.imp import Imp


def version():
    major, minor, patch = (1, 1, 6)
    print(f'Imp (Image processing CLI)\nVersion: {major}.{minor}.{patch}')


def log(s):
    print(f'IMP: {str(s)}')


def error(s):
    print(f'{colorama.Fore.RED}IMP: Error: {str(s)}{colorama.Style.RESET_ALL}')


def show_help():
    version()
    print("""
Help:
    imp <command> <input-file> <optional flags>

Example: imp convert ~/image.png --ext ico

Commands:
    trim     Remove transparent pixels in the edges of the image.
    convert  Change a file image type.
    resize   Resize a image.
    crop     Crop a part of the image.

Options:
    --width    -w   Width of the output image.
    --height   -h   Height of the output image.
    --top      -t   The top of a crop rect.
    --left     -l   The left of a crop rect.
    --ext      -e   The output extension.
    --out      -o   The output path.
    --version  -v   Show current Imp version.
    --help     -p   Show the help.

""")


def main():
    colorama.init()

    try:
        cli = Cli()

        if cli.flag_exists('version', 'v'):
            version()
            del cli
            return

        if cli.flag_exists('help', 'p'):
            show_help()
            del cli
            return

        command = cli.get_arg(
            1, 'command', ['resize', 'trim', 'crop', 'convert'])

        path = cli.get_arg(2, 'path')
        imp = Imp(path)

        # Flags.
        w = cli.get_flag_value('width', 'w')
        h = cli.get_flag_value('height', 'h')
        t = cli.get_flag_value('top', 't')
        l = cli.get_flag_value('left', 'l')
        e = cli.get_flag_value('ext', 'e')
        o = cli.get_flag_value('out', 'o')

        if o != None:
            imp.set_path(o)
        if e != None:
            imp.set_extension(e)

        if command == 'resize':
            imp.resize(w, h)
            imp.save()
            log(f'Image resized with success in "{imp.get_path()}"!')

        elif command == 'crop':
            imp.crop(l, t, w, h)
            imp.save()
            log(f'Image cropped with success in "{imp.get_path()}"!')

        elif command == 'trim':
            imp.trim()
            imp.save()
            log(f'Image trimmed with success in "{imp.get_path()}"!')

        elif command == 'convert':
            imp.convert(e)
            imp.save()
            log(f'Image converted with success in "{imp.get_path()}"!')

        if cli in locals():
            del cli

        if imp in locals():
            del imp

    except Exception as err:
        show_help()
        error(err)


if __name__ == '__main__':
    main()

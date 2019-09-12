<h1><img src="icon/icon.png" align="left" width="32" height="32">imp</h1>

Image processing for command line interface using [Python3](https://www.python.org/downloads/) and [Pillow](https://pypi.org/project/Pillow/).


---

## How to build (using pipenv)

```batch
pipenv shell
pipenv install
pipenv run PyInstaller imp.spec
```

---

## Usage

```bash
imp <command> <input-file> <optional flags>

# Example:
imp convert ~/image.png --ext ico
```


| Valid commands    ||
|---------|------------------------------------------------------|
| trim    | Remove transparent pixels in the edges of the image. |
| convert | Change a file image type.                            |
| resize  | Resize a image.                                      |
| crop    | Crop a part of the image.                            |  


| Valid optional flags    |||
|-----------|----|--------------------------------------------------------------------------------------------|
| --width   | -w | Width of the output image.                                                                 |
| --height  | -h | Height of the output image.                                                                |
| --top     | -t | The top of a crop rect.                                                                    |
| --left    | -l | The left of a crop rect.                                                                   |
| --ext     | -e | The output extension (Could be: 'PNG', 'PPM', 'JPEG', 'JPG', 'GIF', 'TIFF', 'BMP', 'ICO'). |
| --out     | -o | The output path.                                                                           |
| --version | -v | Show current Imp version.                                                                  |
| --help    | -p | Show the help.                                                                             |  


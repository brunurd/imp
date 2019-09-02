<h1><img src="icon/icon.png" align="left" width="32" height="32">&nbsp;&nbsp;imp</h1>
Python 3 image processing cli.


---

## How to build (using pipenv)

```batch
pipenv shell
pipenv install
python -m PyInstaller imp.spec
```

---

## How to use?

Trim transparent pixels of a image.
```batch
imp trim "image-path-here.png"
```

Resize any image.
```batch
imp resize "image-path-here.png" --width 256 --height 256
```

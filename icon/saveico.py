from PIL import Image
filename = r'icon.png'
img = Image.open(filename)
img.save('../imp.ico')
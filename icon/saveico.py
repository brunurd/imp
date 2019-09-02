from PIL import Image

input_path = r'icon.png'
output_path = r'../imp.ico'

image = Image.open(input_path)
image.save(output_path)
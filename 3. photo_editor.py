from PIL import Image,ImageEnhance,ImageFilter
import os

path = "./imgs"
pathout = "./editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SMOOTH)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathout}/{clean_name}_edited.jpg')
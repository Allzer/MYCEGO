import os
from os import listdir
from PIL import Image

dir1 = '1369_12_Наклейки 3-D_3'
dir2 = '1388_2_Наклейки 3-D_1'
dir3 = '1388_6_Наклейки 3-D_2'
dir4 = '1388_12_Наклейки 3-D_3'

dirs = [dir1, dir2, dir3, dir4]
images = []
def create_dir():
    for dir in dirs:
        if not os.path.exists(f"Result\\{dir}"):
            os.makedirs(f"Result\\{dir}")

def change_img():
    for dir in dirs:
        folder_dir = f"Для тестового\\{dir}"
        for image in os.listdir(folder_dir):
            if image.endswith(".png"):
                img = Image.open(f"{folder_dir}\\{image}")
                name, ext = os.path.splitext(image)
                img.save(f"Result\\{dir}\\{name}.tiff")


create_dir()
change_img()
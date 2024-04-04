import os
from os import listdir
import matplotlib.pyplot as plt
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
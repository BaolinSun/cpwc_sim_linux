import os
import re
import cv2
import time
import logging
import matlab
import matlab.engine
import multiprocessing

from multiprocessing import Process
from utils.phantom import PhantomGenerator
from utils.logger import create_logger

mateng = matlab.engine.start_matlab('-nodesktop -nodisplay')
mateng.cd("/home/hrzy/Desktop/CPWC/matlab_script")

raw_data_path = '/home/hrzy/Desktop/CPWC/dataset/train/rfdata'
root_path = '/home/hrzy/Desktop/CPWC/dataset/train'
usimage_path_angle1 = os.path.join(root_path, 'usimage_angle1')
usimage_path_angle3 = os.path.join(root_path, 'usimage_angle3')
usimage_path_angle5 = os.path.join(root_path, 'usimage_angle5')
usimage_path_angle7 = os.path.join(root_path, 'usimage_angle7')

raw_data_list = os.listdir(raw_data_path)
raw_data_list.sort(key= lambda x: int(x[7:]))

for item in raw_data_list:
    raw_data_dir = os.path.join(raw_data_path, item)
    if len(os.listdir(raw_data_dir)) != 75:
        continue

    index = int(re.findall("\d+", item)[0])

    usimage_path = os.path.join(usimage_path_angle1, f'usimage_{index}.png')
    print(usimage_path)
    mateng.reconstruct_img_with_angleID(raw_data_dir, usimage_path, 1)

    usimage_path = os.path.join(usimage_path_angle3, f'usimage_{index}.png')
    print(usimage_path)
    mateng.reconstruct_img_with_angleID(raw_data_dir, usimage_path, 3)

    usimage_path = os.path.join(usimage_path_angle5, f'usimage_{index}.png')
    print(usimage_path)
    mateng.reconstruct_img_with_angleID(raw_data_dir, usimage_path, 5)

    usimage_path = os.path.join(usimage_path_angle7, f'usimage_{index}.png')
    print(usimage_path)
    mateng.reconstruct_img_with_angleID(raw_data_dir, usimage_path, 7)




# addpath('matlab_script')

# raw_data_dir = '/home/hrzy/Desktop/CPWC/dataset/train/rfdata/rfdata_0';
# usimage_path = 'test.png';
# angle_num = 75;

# reconstruct_img_with_angleID(raw_data_dir, usimage_path, angle_num)

# rmpath('matlab_script')
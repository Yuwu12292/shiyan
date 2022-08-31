#导入模块
import os,sys                       
import os
from re import L
import numpy as np
from shapely.geometry import Polygon
from PIL import Image
from tqdm import tqdm
import json
import pdb
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import os
import shutil
import cv2
import os
import re
from glob import glob

import argparse
import yaml
# from new_integrate import new_integrate
from read_yaml import read_yaml
path = 'editordata.yaml'
args = read_yaml(path)
# determination1 = args['determination1']
# print('determination1')

# default = args['determination1']['default']
# print(default)
# print(args.determination1)
import argparse
parser = argparse.ArgumentParser(description="将CORE中不存在于old(data1_path)中的play_back(dat2_path)文件,存储在target(determiantion)中,并更新Old文件夹内容")

parser.add_argument('--determination1',type=str,default=args['determination1']['default'],help='选出的新视频存放路径')
args = parser.parse_args()
print(args.determination1)
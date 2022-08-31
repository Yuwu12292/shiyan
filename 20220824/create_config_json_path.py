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
import glob
from pathlib import Path

import argparse
import ast

import jsonpath
import pprint
def create_config_json_path():
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
   
    from read_yaml import read_yaml
    path = 'editordata.yaml'
    args = read_yaml(path)
    parser = argparse.ArgumentParser(description="上传前整合图片到一个文件夹")
    parser.add_argument('--determination1',type=str,default=args['determination1']['default'],help='要被整合到一个文件夹的图片存储总路径')
    parser.add_argument('--path',type=str,default=args['path']['default'],help='要被整合到一个文件夹的图片存储总路径')
    args = parser.parse_args()
    path=args.path
    create_config_json_path()

    with open('config_.json','r') as f:
        obj = json.load(f)#['preprocessor']['video_writter']['path']
    pprint.pprint(obj)#  pprint.p
    out_nm=args.determination1+'/'+"config.json"
    obj['preprocessor']['video_writter']['path']=args.path
    obj =str(obj)
    obj = obj.replace('\'', '\"')
    obj = obj.replace('False','false')
    obj = obj.replace('True','true')
    obj=obj+"\n"
    with open(out_nm, 'w') as f:
        f.write(obj)
    with open(out_nm,'r') as f:
        out = json.load(f)
    pprint.pprint(out)   
    source='stream_filter'
    deter=args.determination1+'/'+'stream_filter'
    shutil.copyfile(source, deter)





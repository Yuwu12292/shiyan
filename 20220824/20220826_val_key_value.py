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


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description="将CORE中不存在于old(data1_path)中的play_back(dat2_path)文件,存储在target(determiantion)中,并更新Old文件夹内容")
    from read_yaml import read_yaml
    path = 'editordata.yaml'
    args = read_yaml(path)
    parser.add_argument('--coco_val_json_name',type=str,default=args['coco_val_json_name']['default'],help='存储所有图片的字典文件')
    parser.add_argument('--zip_json_path',type=str,default=args['zip_json_path']['default'],help='存待生成整合json的文件')
    parser.add_argument('--zip_json_valid_path',type=str,default=args['zip_json_valid_path']['default'],help='存已经是测试集字典里val_key_value内待整合json,这个可以运行后直接删除')
    parser.add_argument('--val_key_value_name',type=str,default=args['val_key_value_name']['default'],help='存储所有测试集json的字典文件')
    args = parser.parse_args()
    val_key_value={}#args.val_key_value_name
    with open(args.coco_val_json_name,'r') as f:
        coco_val_json=json.load(f)#['preprocessor']['video_writter']['path']
        for i in range(len(coco_val_json['images'])):
            val_key_value[coco_val_json['images'][i]['file_name'].rsplit('.',1)[0]]=coco_val_json['images'][i]['file_name'].rsplit('.',1)[0]+".json"
            # print(val_key_value[coco_val_json['images'][i]['file_name'].rsplit('.',1)[0]])
            # pdb.set_trace()
    # print(len(val_key_value))
    np.save(args.val_key_value_name,val_key_value)#注意带上后缀名
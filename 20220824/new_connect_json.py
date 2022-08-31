#导入模块
from __future__ import annotations
import os,sys                       
import os
from re import L
from unicodedata import category
from venv import create
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
import matplotlib.image as pli
import argparse
def open_json(path,imagess,annotationss,categoriess):
    with open(path, 'r') as fcc_file_new:#打开了json文件
        fcc_data = json.load(fcc_file_new)#读取了json文件内内容，有点像字典
        print(len(fcc_data['images']))
        print(len(fcc_data['annotations']))
        print(fcc_data.keys())
        imagess_0=fcc_data['images']
        annotations_0=fcc_data['annotations']
        categories_0=fcc_data['categories']
        for im in imagess_0:
            imagess.append(im)
        for an in annotations_0:
            annotationss.append(an)
        for ca in categories_0:
            categoriess.append(ca)
if __name__ == '__main__':
    imagess=[]
    annotationss=[]
    categoriess=[]
    from read_yaml import read_yaml
    path = 'editordata.yaml'
    args = read_yaml(path)
    parser = argparse.ArgumentParser(description="任意拼接选中的json,必要时生成val字典")

    parser.add_argument('--coco_val_json_name',type=str,default=args['coco_val_json_name']['default'],help='训练集json文件')
    parser.add_argument('--path_list',type=str,default=args['path_list']['default'],help='要被整合到一个文件夹的图片存储总路径')
    parser.add_argument('--create_val_key',type=str,default=args['create_val_key']['default'],help='是否创建测试集字典文件:"yes" or "no"')
    parser.add_argument('--new_val_key_value_name',type=str,default=args['new_val_key_value_name']['default'],help='存储当前所有测试集json的字典文件')
    args = parser.parse_args()


    coco_val_json_name = args.coco_val_json_name    
    path_list=args.path_list
    for i in path_list:
        # print(i)
        open_json(i,imagess,annotationss,categoriess)
        print(len(annotationss))
        print(categoriess)
    out_path=coco_val_json_name
    out_nm={}
    with open(out_path, 'w') as f:
        out_nm['images']=imagess
        out_nm['annotations']=annotationss
        out_nm['categories']=categoriess
        json.dump(out_nm, f)
    print("out_nm['images']",len(out_nm['images']))
    print("out_nm['annotations']",len(out_nm['annotations']))
    print("out_nm['categories']",len(out_nm['categories']))
    create_val_key=args.create_val_key
    val_key_value={}
    if create_val_key=='yes':
            # 只有真的要生成val_key时，才用这句话
            for ann_nm in imagess:
                val_key_value[ann_nm['file_name'].rsplit('.',1)[0]]=ann_nm['file_name'].rsplit('.',1)[0]+'.json'
            np.save(args.new_val_key_value_name,val_key_value)#注意带上后缀名
            print('测试集字典已更新')

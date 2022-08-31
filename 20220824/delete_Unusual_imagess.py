#导入模块
from __future__ import annotations
from asyncio import exceptions
from logging import exception
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
import matplotlib.image as pli
import argparse
import traceback
def delete_Unusual_imagess():
    folders=glob.glob(Raw_label_root+'/**',recursive=True)#循环遍历
    num=0
    for folder in folders:
        file=folder.rsplit('/',1)[1]#取出folders中某个的'/'后file
        # print(file)
        if len(file.rsplit('.',1))>1:
            num=num+1
            if file in file1_list:      
                shutil.move(folder, move_path+'/' + file)          # 移动文件
                print('已移动文件--',str(num)+'-->'+file)
            else:
                # print('文件无问题')
                continue
        else:
            continue
    print("文件总数为——————————",num)

if __name__ == '__main__': 
        parser = argparse.ArgumentParser(description="根据指定数字范围生成训练集和测试集,也可生成单日的coco文件")
        from read_yaml import read_yaml
        path = 'editordata.yaml'
        args = read_yaml(path)
        parser.add_argument('--Raw_label_root',type=str,default=args['Raw_label_root']['default'],help='所有json总路径————Raw_label路径')
        parser.add_argument('--Unusual_imagess',type=str,default=args['Unusual_imagess']['default'],help='Raw_label文件夹')
        parser.add_argument('--move_path',type=str,default=args['move_path']['default'],help='有问题的Raw_label文件夹')
        args = parser.parse_args()
        Raw_label_root=args.Raw_label_root
        Unusual_imagess=np.load(args.Unusual_imagess,allow_pickle=True).item()
        file1_list=Unusual_imagess.values()
        print(file1_list)
        move_path=args.move_path
        delete_Unusual_imagess()
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

import traceback
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
# coco=COCO('/mnt/RDTeam/01_BDAI/yanglaoyuan_data/Train_val_split/coco_20220819_val.json')
# catIds = coco.getCatIds(catNms=['person','bed']);#catNms=['person','bed']--->[2, 3]
# imgIds = coco.getImgIds(catIds=catIds);
with open('/mnt/RDTeam/01_BDAI/yanglaoyuan_data/Train_val_split/coco_20220819_val.json', 'r') as fcc_file_new:#打开了json文件
    fcc_data = json.load(fcc_file_new)#读取了json文件内内容，有点像字典
    # out_nm = '/mnt/RDTeam/01_BDAI/yanglaoyuan_data/Train_val_split/coco_20220819_val_24.json'
    print(len(fcc_data['images']))
    print(len(fcc_data['annotations']))
    print(fcc_data.keys())
    imagess=fcc_data['images']
    annotations=fcc_data['annotations']
    categories=fcc_data['categories']

# for i in imgIds:
#     # print(i)
#     imgIds = coco.getImgIds(imgIds=i)
#     img=coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
    i=0
    j=0
    # except_imagess={}#不行，不能直接取，复杂化了
    # except_annotations={}
    Unusual_imagess={}
    imagess=fcc_data['images']
    for num in range(len(imagess)):

        pic=imagess[num]['file_name']
        img=imagess[num]['local_path']
        try:
            # print(img,"--->",i)
            # pdb.set_trace()
            im=plt.imread(img) #第0个图片
            im=Image.fromarray(im)   #正常应该是image.open()
            print(im,"-->",i)
            plt.imshow(im)
            plt.show()
            i=i+1
            # except_imagess[j]=imagess[num]
            # except_annotations[j]=
            # j=j+1
        except:
            print("出错啦")
            print(img,"--->",i)
            print(pic.rsplit('.',1)[0])
            Unusual_imagess[num]=pic.rsplit('.',1)[0]+'.json'
            continue
print(Unusual_imagess.keys())
np.save('Unusual_imagess.npy',Unusual_imagess)
# for i in range(len(imgIds)):
#     print(i)
# # imgIds = coco.getImgIds(imgIds = [5400])
# # print(imgIds)#-->[100]
# # print(imgIds[np.random.randint(0,len(imgIds))])
# img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
# # print(img)#-->{'file_name': 'D40_20211210055959_07340.jpg', 'height': 360, 'width': 640, 'id': 100, 'local_path': '/home/scripts/data/jpg/D40_20211210055959_07340.jpg'}
# I = io.imread(img['local_path'])
# plt.axis('off')
# plt.imshow(I)
# plt.show()
# # with open('/mnt/RDTeam/01_BDAI/yanglaoyuan_data/Train_val_split/coco_20220819_val.json', 'r') as fcc_file_new:#打开了json文件
# #     fcc_data = json.load(fcc_file_new)#读取了json文件内内容，有点像字典
# #     # out_nm = '/mnt/RDTeam/01_BDAI/yanglaoyuan_data/Train_val_split/coco_20220819_val_24.json'
# #     print(len(fcc_data['images']))
# #     print(len(fcc_data['annotations']))
# #     print(fcc_data.keys())
# #     imagess=fcc_data['images']
# #     annotations=fcc_data['annotations']
# #     categories=fcc_data['categories']
# #     #用于删除有问题
# #     # print(imagess[7510])
# #     # print(annotations[7510])
# #     # del imagess[7510]
# #     # del annotations[7510]
# #     # fcc_data['images']=imagess
# #     # fcc_data['annotations']=annotations
# #     # with open(out_nm, 'w') as f:
# #     #     json.dump(fcc_data, f)

# try:    #逐个输出图片
#     i=0
#     imagess=fcc_data['images']
#     for num in range(len(imagess)):
#         pic=imagess[num]['file_name']
#         img=imagess[num]['local_path']
#         print(img,"--->",i)
#         # pdb.set_trace()
#         im=plt.imread(img) #第0个图片
#         im=Image.fromarray(im)   #正常应该是image.open()
#         print(im)
#         plt.imshow(im)
#         plt.show()
#         i=i+1
# except (ValueError, ArithmeticError):
#     print("程序发生了数字格式异常、算术异常之一")
# except :
#     print("未知异常")
#     continue
# print("程序继续运行")
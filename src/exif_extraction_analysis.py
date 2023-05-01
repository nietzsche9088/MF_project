from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    return exif_table

import pandas as pd 
import os

for dname in ['CASIA', 'Columbia', 'DSO', 'NIST16']:
    for pname in ['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]:
        exif0 = []
        exif1 = []
        imgs = os.listdir(os.path.join(path, dname, dname))
        for img in imgs:
            ori_path = os.path.join(path, dname, dname, img)
            exif0.append(get_exif(ori_path))
            
            if os.path.isfile(os.path.join(path, dname, pname, img)):      #casia, nist
                plaf_path = os.path.join(path, dname, pname, img)
            elif os.path.isfile(os.path.join(path, dname, pname, img.rsplit('.', 1)[0]+'.jpg')):    #other jpg
                plaf_path = os.path.join(path, dname, pname, img.rsplit('.', 1)[0]+'.jpg')
            elif os.path.isfile(os.path.join(path, dname, pname, img.rsplit('.', 1)[0]+'.jpeg')):    #whatsapp
                plaf_path = os.path.join(path, dname, pname, img.rsplit('.', 1)[0]+'.jpeg')
            else:
                print('error')
            exif1.append(get_exif(plaf_path))  
        print( pname, exif0)
        break
            
from PIL import Image
import numpy as np
import cv2
import math
from matplotlib import pyplot as plt
import os
from statistics import mode

def calculate_probability(s, n, e):
    if s >= n/2:
        return 0.0


    log_term = n * math.log10((s*e)/n) + (-1/2) * math.log10(2*math.pi*n)

    exp_term = -2 * (((n/2) - s)**2 / n) * math.log10(math.e)

    probability = 10**(min(log_term, exp_term))

    return probability

def obtain_QT(img_path):
    img = np.array(Image.open(img_path))
    plt.imshow(img)
    plt.show()
    QT, NFA = [], []
    Y = np.round(0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2])

    height, width= Y.shape[:2]
    block_size = 8
    block_rows = height // block_size
    block_cols = width // block_size

    for c in range(1,64):
        for q in range(1, 256):
            s, n = 0, 0
            for row in range(0, block_rows):
                for col in range(0, block_cols):
                    tmp = np.float32(Y[row*block_size:(row+1)*block_size, col*block_size:(col+1)*block_size])
                    v = cv2.dct(tmp).flatten()[c]
                    V = np.round(v/q)
                    if V != 0:
                        e = 2*np.linalg.norm((v/q) - V)
                        s = s + e
                        n = n + 1

            nfa = 64*63*255*(calculate_probability(s, n, e))
            print(nfa, NFA, c)
            if nfa <= 1 and nfa < NFA[c]:
                Q[c] = q
                NFA[c] = nfa
    return QT

path = './dataset'

for dname in ['CASIA', 'Columbia', 'DSO', 'NIST16']:
    QT_list = []
    label_list = []
    for pname in ['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]:
        imgs = os.listdir(os.path.join(path, dname, pname))
        for img in imgs:
            img_path = os.path.join(path, dname, pname, img)
            qt = obtain_QT(img_path)
            QT_list.append(qt)
            label_list.append(pname)

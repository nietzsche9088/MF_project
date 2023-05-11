import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from PIL import Image
from tqdm import tqdm
import os

path = '../dataset'
size = (256, 256)
for dname in tqdm(['CASIA', 'Columbia', 'DSO',  'NIST16']):
    noise_list, labels_list = [], []
    for pname in tqdm(['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]):
            imgs = os.listdir(os.path.join(path, dname, pname))
            for img in tqdm(imgs):

                if dname == 'Columbia':
                    ori = np.array(Image.open(os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.tif')).convert('RGB').resize(size))
                elif dname == 'DSO':
                    ori = np.array(Image.open(os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.png')).convert('RGB').resize(size))
                elif pname == 'CASIA_Whatsapp' or pname == 'NIST16_Whatsapp':
                    ori = np.array(Image.open(os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.jpg')).convert('RGB').resize(size))
                else:
                    ori = np.array(Image.open(os.path.join(path, dname, dname, img)).convert('RGB').resize(size))

                im = np.array(Image.open(os.path.join(path, dname, pname, img)).convert('RGB').resize(size))
                noise = np.resize(im, ori.shape) - ori

                noise_list.append(noise)
                labels_list.append(pname)

    features = np.concatenate(noise_list)
#     labels = np.concatenate(labels_list)

    np.save('../extraction/%s_noise_feature1.npy'%dname, features)
    np.save('../extraction/%s_noise_label1.npy'%dname, labels_list)
    
for dataset, length in [('CASIA', 920), ('Columbia', 160), ('DSO', 100), ('NIST16', 564)]:

    feature = np.load('./extraction/%s_noise_feature1.npy'%dataset, allow_pickle=True)
    label = np.load('./extraction/%s_noise_label1.npy'%dataset, allow_pickle=True)


    facebook, wechat, weibo, whatsapp = [], [], [], []
    for i in range(len(label)):
        if label[i] == '%s'%dataset:
            if original == []:
                original = feature[i]
            else:
                original = np.vstack((original, feature[i]))
        elif label[i] == '%s_Facebook'%dataset:
            if facebook == []:
                facebook = feature[i]
            else:
                facebook = np.vstack((list(facebook), list(feature[i])))
        elif label[i] == '%s_Wechat'%dataset:
            if wechat == []:
                wechat = feature[i]
            else:
                wechat = np.vstack((wechat, feature[i]))
        elif label[i] == '%s_Weibo'%dataset:
            if weibo == []:
                weibo = feature[i]
            else:
                weibo = np.vstack((weibo, feature[i]))
        else:
            if whatsapp == []:
                whatsapp = feature[i]
            else:
                whatsapp = np.vstack((whatsapp, feature[i]))

    ordered_feature = np.concatenate((facebook, wechat, weibo, whatsapp), axis = 0)

    tsne = TSNE(n_components = 2, perplexity = 30, learning_rate = 200)
    embedded = tsne.fit_transform(ordered_feature)

    plt. scatter(embedded[0:length, 0], embedded[0:length, 1], c = 'g', marker = 's', label = 'facebook')
    plt. scatter(embedded[length:length*2, 0], embedded[length:length*2, 1], c = 'b', marker = '^', label = 'wechat')
    plt. scatter(embedded[length*2:length*3, 0], embedded[length*2:length*3, 1], c = 'y', marker = 'd', label = 'weibo')
    plt. scatter(embedded[length*3:length*4, 0], embedded[length*3:length*4, 1], c = 'm', marker = '*', label = 'whatsapp')
    plt.legend()
    plt.title('Image features from %s dataset visulized by social networks'%dataset)
    plt.savefig('./output/%s_tsne_noise.png'%dataset)
    plt.show()

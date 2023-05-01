import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

dataset = 'CASIA'
length = 920

feature = np.load('./extraction/%s_features1.npy'%dataset)
label = np.load('./extraction/%s_labels1.npy'%dataset)


original, facebook, wechat, weibo, whatsapp = [], [], [], [], []
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
            facebook = np.vstack((facebook, feature[i]))
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
    

ordered_feature = np.concatenate((original, facebook, wechat, weibo, whatsapp), axis = 0)

tsne = TSNE(n_components = 2, perplexity = 30, learning_rate = 200)
embedded = tsne.fit_transform(ordered_feature)

plt. scatter(embedded[:length, 0], embedded[:length, 1], c = 'r', marker = 'o', label = 'original')
plt. scatter(embedded[length:length*2, 0], embedded[length:length*2, 1], c = 'g', marker = 's', label = 'facebook')
plt. scatter(embedded[length*2:length*3, 0], embedded[length*2:length*3, 1], c = 'b', marker = '^', label = 'wechat')
plt. scatter(embedded[length*3:length*4, 0], embedded[length*3:length*4, 1], c = 'y', marker = 'd', label = 'weibo')
plt. scatter(embedded[length*4:length*5, 0], embedded[length*4:length*5, 1], c = 'm', marker = '*', label = 'whatsapp')
plt.legend()
plt.title('Image features from %s dataset visulized by social networks'%dataset)
plt.savefig('./output/%s_tsne1.png'%dataset)
plt.show()
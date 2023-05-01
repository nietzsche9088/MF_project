import os
from PIL import Image
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

path = '../dataset'

for dname in ['CASIA', 'Columbia', 'DSO', 'NIST16']:
    pred_list = []
    gt_list = []
    for pname in ['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]:
        imgs = os.listdir(os.path.join(path, dname, pname))
        for img in imgs:
            gt_list.append(pname)
            
            if img.rsplit('.', 1)[1] == 'jpeg':
                pred_list.append('%s_Whatsapp'%dname)
            else:
                img = Image.open(os.path.join(path, dname, pname, img))
                if max(img.size) == 2048:
                    pred_list.append('%s_Facebook'%dname)
                else:
                    pred_list.append(random.choice(['%s_Weibo'%dname, '%s_Wechat'%dname]))
    cm = confusion_matrix(gt_list, pred_list)
    labels = ['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix')
    plt.savefig('../output/%s_confusion_matrix.png'%dname)
    plt.show()


                    
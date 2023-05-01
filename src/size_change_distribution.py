import os
import numpy as np
path = './dataset'
for dname in ['CASIA', 'Columbia', 'DSO', 'NIST16']:
    for pname in ['%s_Facebook'%dname, '%s_Wechat'%dname, '%s_Weibo'%dname, '%s_Whatsapp'%dname]:
        imgs = os.listdir(os.path.join(path, dname, pname))
        sizelist = []
        for img in imgs:
            if pname == '%s_Whatsapp'%dname:
                oripath = os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.jpg')
            else:
                oripath = os.path.join(path, dname, dname, img)
            if dname == 'Columbia':
                oripath = os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.tif')
            elif dname == 'DSO':
                oripath = os.path.join(path, dname, dname, img.rsplit('.', 1)[0] + '.png')                
            filepath = os.path.join(path, dname, pname, img)
            with open(oripath, "rb") as f:
                    orisize = len(f.read())
            with open(filepath, "rb") as f:
                    filesize = len(f.read())   
            sizelist.append(orisize-filesize)
        print('%s ave size difference: '%pname, np.mean(sizelist))
        
        
import os
import numpy as np
import matplotlib.pyplot as plt
path = './dataset'
for dname in ['CASIA', 'Columbia', 'DSO', 'NIST16']:
    imgs = os.listdir(os.path.join(path, dname, dname))
    ori, fb, wc, wb, wa = [], [], [], [], []
    for img in imgs:
        oripath = os.path.join(path, dname, dname, img)
        with open(oripath, "rb") as f:
                ori.append(len(f.read())/1e6)
                
        if os.path.isfile(os.path.join(path, dname, '%s_Facebook'%dname, img.rsplit('.', 1)[0]+'.jpg')):
            with open(os.path.join(path, dname, '%s_Facebook'%dname, img.rsplit('.', 1)[0]+'.jpg'), "rb") as f:
                fb.append(len(f.read())/1e6)
        elif os.path.isfile(os.path.join(path, dname, '%s_Facebook'%dname, img.rsplit('.', 1)[0]+'.jpeg')):
            with open(os.path.join(path, dname, '%s_Facebook'%dname, img.rsplit('.', 1)[0]+'.jpeg'), "rb") as f:
                fb.append(len(f.read())/1e6)   
                
        if os.path.isfile(os.path.join(path, dname, '%s_Wechat'%dname, img.rsplit('.', 1)[0]+'.jpg')):
            with open(os.path.join(path, dname, '%s_Wechat'%dname, img.rsplit('.', 1)[0]+'.jpg'), "rb") as f:
                wc.append(len(f.read())/1e6)
        elif os.path.isfile(os.path.join(path, dname, '%s_Wechat'%dname, img.rsplit('.', 1)[0]+'.jpeg')):
            with open(os.path.join(path, dname, '%s_Wechat'%dname, img.rsplit('.', 1)[0]+'.jpeg'), "rb") as f:
                wc.append(len(f.read())/1e6)  
                
        if os.path.isfile(os.path.join(path, dname, '%s_Weibo'%dname, img.rsplit('.', 1)[0]+'.jpg')):
            with open(os.path.join(path, dname, '%s_Weibo'%dname, img.rsplit('.', 1)[0]+'.jpg'), "rb") as f:
                wb.append(len(f.read())/1e6)
        elif os.path.isfile(os.path.join(path, dname, '%s_Weibo'%dname, img.rsplit('.', 1)[0]+'.jpeg')):
            with open(os.path.join(path, dname, '%s_Weibo'%dname, img.rsplit('.', 1)[0]+'.jpeg'), "rb") as f:
                wb.append(len(f.read())/1e6)  
                
        if os.path.isfile(os.path.join(path, dname, '%s_Whatsapp'%dname, img.rsplit('.', 1)[0]+'.jpg')):
            with open(os.path.join(path, dname, '%s_Whatsapp'%dname, img.rsplit('.', 1)[0]+'.jpg'), "rb") as f:
                wa.append(len(f.read())/1e6)
        elif os.path.isfile(os.path.join(path, dname, '%s_Whatsapp'%dname, img.rsplit('.', 1)[0]+'.jpeg')):
            with open(os.path.join(path, dname, '%s_Whatsapp'%dname, img.rsplit('.', 1)[0]+'.jpeg'), "rb") as f:
                wa.append(len(f.read())/1e6)  
        
#     plt.plot(ori, label=dname)
#     plt.plot(fb, label='Facebook')
#     plt.plot(wc, label='Wechat')
#     plt.plot(wb, label='Weibo')
#     plt.plot(wa, label='Whatsapp')

#     plt.xlabel('Images')
#     plt.ylabel('Size(MB)')
#     plt.title('%s Image Size Distribution'%dname)
#     plt.legend(loc = 1)
#     plt.savefig('./output/%s_size_distribution.png'%dname, bbox_inches="tight")
#     plt.show()

    bar_width = 0.15
    x_pos = np.arange(len(ori))
    plt.bar(x_pos - 2 * bar_width, ori, width=bar_width, align='center', label=dname)
    plt.bar(x_pos - bar_width, fb, width=bar_width, align='center', label='Facebook')
    plt.bar(x_pos, wc, width=bar_width, align='center', label='Wechat')
    plt.bar(x_pos + bar_width, wb, width=bar_width, align='center', label='Weibo')
    plt.bar(x_pos + 2 * bar_width, wa, width=bar_width, align='center', label='Whatsapp')

    plt.xticks([],[])
    plt.xlabel('Images')
    plt.ylabel('Size(MB)')
    plt.title('%s Image Data Size'%dname)
    plt.legend(loc = 1)
    plt.savefig('./output/%s_size_data.png'%dname, bbox_inches="tight")
    plt.show()


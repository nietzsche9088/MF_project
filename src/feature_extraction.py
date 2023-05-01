import torch
import torchvision.models as models
from torchvision import transforms
from dataloader import myDataset, custom_collate
from torch.utils.data import Dataset, DataLoader
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 


def extract_features(images, model):

    with torch.no_grad():
        features = model(images)
        features = torch.flatten(features, 1)

    return features.numpy()


resnet = models.resnet50(pretrained=True)

resnet.eval()

for datasetname in [ 'NIST16', 'Columbia']:#'CASIA', 'DSO',
    features_list = []
    labels_list = []
    dataset = myDataset('../dataset/%s'%datasetname, transforms.Compose([
            
            transforms.ToTensor()


        ]))
#     transforms.Resize(256),
#             transforms.CenterCrop(224),            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True, collate_fn=custom_collate)
    print('------------Loading dataset %s-------------'%datasetname)
    for images, labels in dataloader:
        features = extract_features(images, resnet)
        features_list.append(features)
        labels_list.append(labels)
    print('-----------Extracting feature-----------')

    features = np.concatenate(features_list)
    labels = np.concatenate(labels_list)

    np.save('./extraction/%s_features_test.npy'%datasetname, features)
    np.save('./extraction/%s_labels_test.npy'%datasetname, labels)
    print('-----------Saving features and labels-----------')

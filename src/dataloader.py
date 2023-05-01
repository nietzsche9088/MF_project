import os
from PIL import Image
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


def custom_collate(batch):
    images = []
    labels = []
    for img, label in batch:
        images.append(torch.tensor(np.array(img)).unsqueeze(0).float())
        labels.append(label)
    return torch.cat(images, dim=0), labels



class myDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.transform = transform
        self.root_dir = root_dir
        self.img_files = []
        self.labels = []
        for label in os.listdir(root_dir):
            label_path = os.path.join(root_dir, label)
            if os.path.isdir(label_path):
                for img_file in os.listdir(label_path):
                    img_path = os.path.join(label_path, img_file)
                    self.img_files.append(img_path)
                    self.labels.append(label)

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, index):
        img_path = self.img_files[index]
        label = self.labels[index]
        with open(img_path, 'rb') as f:
            img = Image.open(f)
            img = img.convert('RGB')                   #.resize((256,256))
        if self.transform is not None:
            img = self.transform(img)
        return img, label


# dataset = myDataset('./dataset/NIST')
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True, collate_fn=custom_collate)

# for batch_idx, (data, labels) in enumerate(dataloader):
#     print(f"Batch {batch_idx}:")
#     print("Data shape:", data.shape)
#     print("Labels:", labels)

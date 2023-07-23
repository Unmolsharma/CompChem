import torch
import torchvision
from torch.utils.data import Dataset


class CIFAR10Dataset(Dataset):
    def __init__(self, transform=None):
        self.dataset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True)
        self.transform = transform

    def __getitem__(self, index):
        image, label = self.dataset[index]

        if self.transform:
            image, label = self.transform((image, label))

        return image, label

    def __len__(self):
        return len(self.dataset)


class ToTensor:
    def __call__(self, sample):
        image, label = sample
        image = torchvision.transforms.ToTensor()(image)
        return image, label


print('Without Transform')
dataset = CIFAR10Dataset()
first_data = dataset[0]
image, label = first_data
print(type(image), type(label))
print(image.size, label)

print('\nWith Tensor Transform')
dataset = CIFAR10Dataset(transform=ToTensor())
first_data = dataset[0]
image, label = first_data
print(type(image), type(label))
print(image.size(), label)

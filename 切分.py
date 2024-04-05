import os
import torch
from torchvision import datasets, transforms
from torchvision.utils import save_image
from tqdm import tqdm
import math

def data_split(scr_data_path, traget_data_path, train_scale, val_scale, test_scale, num_workers, img_format):
    data = datasets.ImageFolder(scr_data_path, transforms.ToTensor())
    class_name = list(data.class_to_idx.keys())
    image_size = len(data)
    print("总计:" + str(image_size) + "it")
    train_size = math.ceil(image_size * train_scale)
    test_size = min(image_size - train_size, math.ceil(image_size * test_scale))
    val_size = min(image_size - train_size - test_size, math.ceil(image_size * val_scale))
    loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=True, num_workers=num_workers)
    for C in class_name:
        if not os.path.isdir(os.path.join(traget_data_path, 'train', C)) and train_scale:
            os.makedirs(os.path.join(traget_data_path, 'train', C))
        if not os.path.isdir(os.path.join(traget_data_path, 'test', C)) and test_scale:
            os.makedirs(os.path.join(traget_data_path, 'test', C))
        if not os.path.isdir(os.path.join(traget_data_path, 'val', C)) and val_scale:
            os.makedirs(os.path.join(traget_data_path, 'val', C))
    for index, image in tqdm(enumerate(loader)):
        image, label = image
        while train_size > 0:
            save_image(image,
                       os.path.join(traget_data_path, 'train', class_name[label], str(index + 1) + '.' + img_format))
            train_size -= 1
            break
        while test_size > 0 and not train_size:
            save_image(image,
                       os.path.join(traget_data_path, 'test', class_name[label], str(index + 1) + '.' + img_format))
            test_size -= 1
            break
        while val_size > 0 and not test_size:
            save_image(image,
                       os.path.join(traget_data_path, 'val', class_name[label], str(index + 1) + '.' + img_format))
            val_size -= 1
            break
    print("切分完成\n保存路径为：" + traget_data_path)


if __name__ == '__main__':
    data_split(
        scr_data_path=r"D:\pythonProject\STUDY\bishe\cata",  # 原始数据集路径
        traget_data_path=r'D:\pythonProject\STUDY\bishe\shujuji',  # 保存切分后数据集的保存路径
        train_scale=0.7,  # 训练集数量占比
        test_scale=0.2,  # 测试集数量占比
        val_scale=0.1,  # 验证集数量占比
        num_workers=12,  # 线程数 越大越快
        img_format='jpg',  # 想要保存的图像格式 'jpg' or 'png'
    )
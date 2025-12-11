# 项目结构：
````
├──task 1
   └── bus.jpg
   └── 任务1result.jpg
   └── YOLO任务1.py
├──task 2
   └── surrounding.mp4
   └── 任务2result.mp4
   └── YOLO任务2.py
├──task 3
   └── traffic_test.jpg
   └── 任务3result.jpg
   └── YOLO任务3.py
   └── runs
   └── data_1.yaml
├──task 4
   └── 任务4result.mp4 
├──advanced task 1
   └── YOLO12n模型结果.jpg
   └── YOLOv8n模型结果.jpg
   └── YOLO进阶任务1.py
├──advanced task 2
   └── drone_test.jpg
   └── 进阶任务2result.jpg
   └── YOLO进阶任务2.py
   └── runs
   └── VisDrone.yaml
├──yolov8n.pt  
├──yolo11n.pt
├──yolo12n.pt
├──README.md
├──笔记.md
````
# 项目使用的数据集：

## 任务3中的数据集：
````
import kagglehub

# Download latest version
path = kagglehub.dataset_download("ashfakyeafi/road-vehicle-images-dataset")

print("Path to dataset files:", path)
````
*由于是从kaggle网站上下载，需要运行上述代码以下载数据集*

## 进阶任务2中的数据集：
[VisDrone](https://ai-studio-online.bj.bcebos.com/v1/files/d78ec7b3e6f6446f84071d0762ab2ea4cc0c4c5fd7a9490fb34a0ea8dff05071?responseContentDisposition=attachment%3Bfilename%3Dvisdrone2019.zip&authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2025-12-04T12%3A57%3A44Z%2F60%2F%2Ffc0982da63ae6c1f8685b8c4e496b242c0397ada9ef45aed272301cbd9ae1412)

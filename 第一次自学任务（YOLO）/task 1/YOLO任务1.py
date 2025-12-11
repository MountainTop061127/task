from ultralytics import YOLO
import cv2

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 打开图片
img_path = r"C:\Users\xzt77\Desktop\ComSen\第一次自学任务（YOLO）\task 1\bus.jpg"
# 用的豆包生成的图片
img = cv2.imread(img_path)

# 加载模型
model = YOLO(r"yolov8n.pt")
model.to('cuda')

# 图像检测
results = model(img)

# 显示图像
result_img = results[0].plot()
cv2.imshow("result", mat=result_img)
cv2.waitKey(0)
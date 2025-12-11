from ultralytics import YOLO
import cv2

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 加载模型
model = YOLO(r"yolov8n.pt")
model.to('cuda')

# 视频文件
video_path = r"C:\Users\xzt77\Desktop\ComSen\第一次自学任务（YOLO）\task 2\surrounding.MP4"
# 手机录的

# 打开视频
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # 获取图像
    video, frame = cap.read()
    # 如果读取成功
    if video:
        # 调用模型（一帧一帧处理）
        results = model(frame)

        # 绘制结果
        result_frame = results[0].plot()

        # 显示图像
        cv2.imshow(winname="result", mat=result_frame)

        # 按ESC退出
        if cv2.waitKey(1) == 27:
            break

    else:
        break

# 释放链接
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
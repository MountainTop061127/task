from ultralytics import YOLO
import cv2

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = YOLO(r"yolo11n.pt")
    model.train(
        data=r"D:\Anaconda\project\VisDrone\VisDrone.yaml",
        epochs=30,
        imgsz=640,
        batch=-1,# batch=-1时会自动选择最佳batch size
        name='custom_yolo',
        cache=False,# 设置为“ram”速度反而增加了2~3s，内存占用还贼大，16G内存直接爆了
        workers=1,# 多进程   从2min+ ——> 20s，若大于1则速度反而下降
        device="0",
    )

    metrics = model.val()
    print(f"mAP50: {metrics.box.map50}")
    print(f"mAP50-95: {metrics.box.map}")

    # 打开图片
    img_path = r"C:\Users\xzt77\Desktop\ComSen\第一次自学任务（YOLO）\advanced task 2\drone_test.png"
    # 用的豆包生成的图片
    img = cv2.imread(img_path)
    model = YOLO('runs/detect/custom_yolo/weights/best.pt')
    results = model(img)

    # 显示图像
    result_img = results[0].plot()
    cv2.imshow("result", mat=result_img)
    cv2.waitKey(0)
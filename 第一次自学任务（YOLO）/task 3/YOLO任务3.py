from ultralytics import YOLO
import cv2

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = YOLO(r"YOLOv8n.pt")
    model.train(
        data=r"D:\Anaconda\project\traffic_data\data_1.yaml",
        epochs=50,
        imgsz=640,
        batch=-1,
        name='custom_yolo',
        cache=False,
        workers=1,
        device="0",
    )

    metrics = model.val()
    print(f"mAP50: {metrics.box.map50}")
    print(f"mAP50-95: {metrics.box.map}")

    # 打开图片
    img_path = r"C:\Users\xzt77\Desktop\ComSen\第一次自学任务（YOLO）\task 3\traffic_test.jpg"
    # 用的豆包生成的图片
    img = cv2.imread(img_path)
    model = YOLO('runs/detect/custom_yolo/weights/best.pt')
    results = model(img)

    # 显示图像
    result_img = results[0].plot()
    cv2.imshow("result", mat=result_img)
    cv2.waitKey(0)
from ultralytics import YOLO

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = YOLO(r"yolo12n.pt")
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
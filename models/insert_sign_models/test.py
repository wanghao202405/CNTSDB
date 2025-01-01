import torch
model = torch.hub.load('ultralytics/yolov5', 'custom', path='insert_sign_yolo_best.pt')
results = model('/work/datasets/tt100k45/images/test/7955.jpg')
results.show()
print(results)
# 提取检测结果为DataFrame
df = results.pandas().xyxy[0]  # 获取预测结果的DataFrame格式
# 遍历DataFrame并打印对象的位置和类型
for index, row in df.iterrows():
    # 提取位置和类型
    x_min, y_min, x_max, y_max = row['xmin'], row['ymin'], row['xmax'], row['ymax']
    class_name = row['name']     # 对象类别名称
    confidence = row['confidence']  # 置信度

    print(f"Object: {class_name}, Confidence: {confidence:.2f}, "
          f"Position: x_min={x_min:.2f}, y_min={y_min:.2f}, x_max={x_max:.2f}, y_max={y_max:.2f}")

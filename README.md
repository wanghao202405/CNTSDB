# CNTSDB
## CNTSDB：基于新国标的中国交通标志检测数据集

## 一、重新规划交通标志mark 文件
（1） 60项  指示标志
![img.png](img.png)
（2）141项  禁止标志
![img_1.png](img_1.png)
![img_2.png](img_2.png)

（3）80项  警告标志
![img_3.png](img_3.png)

（4）完整类别
![](marks.png)

## 二、利用TSGAN扩增交通标志
对于无实例和少实例的交通标志，使用TSGAN进行定向扩增
![利用TSGAN 扩增交通标志](https://github.com/user-attachments/assets/cecc26ca-bb6f-4d4e-87b0-2705ca25289a)

## 三、利用YOLO V8 检测交通标志可插入位置
![image](https://github.com/user-attachments/assets/1ed37d65-6b23-4f42-80a4-2272132be82f)


## 四、合适位置插入新的交通标志
![img_4.png](img_4.png)
## 五、新增交通标志例子

#### wels
![image](https://github.com/user-attachments/assets/b4784446-b53b-4c84-8055-d05ca84abcef)

#### wls40
![image](https://github.com/user-attachments/assets/439366f8-c45b-40ae-9d64-ccb142877db1)

#### 雾天
![img_5.png](img_5.png)
## 六、数据集标注信息
数据集采用yolo格式标注
![image](https://github.com/user-attachments/assets/ce526379-18da-48b9-895c-0fdf9ef20ef2)

### 下载地址
链接: 
https://pan.baidu.com/s/1oeeO38RiWldEpAJ3RcImyw?pwd=9qpy
提取码: 9qpy




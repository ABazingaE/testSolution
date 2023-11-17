import math

import numpy as np
import matplotlib.pyplot as plt

## 根据不同的地面倾斜角度表示出地面的直线
#射灯到地面的距离D
def getGroundLine(alpha, D):
    k = np.tan(alpha)
    b = -D
    return k, b

## 根据射灯的开角表示出射灯的直线
def getLightLine(theta):
    k = np.tan(np.pi/2 - theta/2)
    b = 0
    return k, b

## 第三条直线，斜率为第二条直线的斜率的相反数，过原点
def getThirdLine(k):
    b = 0
    return -k, b

## 求直线交点
def getCrossPoint(k1, b1, k2, b2):
    x = (b2 - b1)/(k1 - k2)
    y = k1*x + b1
    return x, y

## 求出两个交点的距离
def getDistance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)



## 画出直线，可视化展示
def draw(k1, b1, k2, b2, k3, b3, spacing):
    plt.ylim(-120, 0)
    plt.xlim(-1300, 1300)

    x = np.linspace(-1300, 1200, 500)
    y1 = k1*x + b1

    plt.plot(x, y1, label="Ground Line")

    # 定义颜色循环
    colors = plt.cm.viridis(np.linspace(0, 1, 9))

    # 画出所有平移后的直线
    for i in range(-4, 5):
        #x_shifted = x - i * spacing
        y2_shifted = k2*x + b2
        y3_shifted = k3*x + b3
        plt.plot(x + i * spacing, y2_shifted, color=colors[i + 4])
        plt.plot(x + i * spacing, y3_shifted, color=colors[i + 4])

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

alpha = math.radians(1.5)
theta = math.radians(120)

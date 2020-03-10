'''
@Description: code
@Author: MiCi
@Date: 2020-03-10 19:59:21
@LastEditTime: 2020-03-10 20:06:48
@LastEditors: MiCi
'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Practice3(object):

    def __init__(self):
        return

    def exercise_1(self):
        '''
        1.绘制x=(0,10)间sin的图像，设置线性为虚线，设置y轴显示范围为(-1.5,1.5)
        2.设置x,y轴标签variable x，value y，设置图表标题“三角函数”，显示网格
        3.绘制平行于x轴y=0.8的水平参考线
        4.绘制垂直于x轴x<4 and x>6的参考区域，以及y轴y<0.2 and y>-0.2的参考区域
        5.添加注释文字sin(x)
        6.用箭头标出第一个峰值
        '''
        plt.subplot(2, 3, 1)
        x1 = np.linspace(0, 10, 100)
        plt.plot(x1, np.sin(x1), '--')
        plt.ylim(-1.5, 1.5)

        plt.subplot(2, 3, 2)
        x2 = np.linspace(0.05, 10, 100)
        y2 = np.sin(x2)
        plt.plot(x2, y2, label='sin(x)')
        plt.xlabel('variable x')
        plt.ylabel('value y')
        plt.title('三角函数')
        plt.grid()

        plt.show()


if __name__ == '__main__':
    print('Practice 3')
    exampleLabel = Practice3()
    exampleLabel.exercise_1()

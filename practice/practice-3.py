'''
@Description: code
@Author: MiCi
@Date: 2020-03-10 19:59:21
@LastEditTime: 2020-03-11 23:39:13
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

        plt.subplot(2, 3, 3)
        x3 = np.linspace(0.05, 10, 100)
        y3 = np.sin(x3)
        plt.plot(x3, y3)
        plt.axhline(y=0.8, ls='--', c='r')

        plt.subplot(2, 3, 4)
        x4 = np.linspace(0.05, 10, 100)
        y4 = np.sin(x4)
        plt.plot(x4, y4)
        plt.axvspan(xmin=4, xmax=6, facecolor='r', alpha=0.3)
        plt.axhspan(ymin=-0.2, ymax=0.2, facecolor='y', alpha=0.3)

        plt.subplot(2, 3, 5)
        x5 = np.linspace(0.05, 10, 100)
        y5 = np.sin(x5)
        plt.plot(x5, y5)
        plt.text(3.2, 0, 'sin(x)', weight='bold', color='r')

        plt.subplot(2, 3, 6)
        x6 = np.linspace(0.05, 10, 100)
        y6 = np.sin(x6)
        plt.plot(x6, y6)
        plt.annotate('maximum', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 1),
                     weight='bold',
                     color='r',
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3',
                                     color='r'))

        plt.show()


if __name__ == '__main__':
    print('Practice 3')
    exampleLabel = Practice3()
    exampleLabel.exercise_1()

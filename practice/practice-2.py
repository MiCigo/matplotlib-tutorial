'''
@Description: code
@Author: MiCi
@Date: 2020-03-10 14:31:33
@LastEditTime: 2020-03-10 19:55:51
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Practice2(object):

    def __init__(self):
        return

    def exercise_1(self):
        '''
        1.用plot方法画出x=(0,10)间sin的图像
        2.用点加线的方式画出x=(0,10)间sin的图像
        3.用scatter方法画出x=(0,10)间sin的点图像
        4.用饼图的面积及颜色展示一组4维数据
        5.绘制一组误差为±0.8的数据的误差条图
        6.绘制一个水平方向柱状图
        '''
        plt.subplot(2, 3, 1)
        x = np.linspace(0, 10, 30)
        plt.plot(x, np.sin(x))

        plt.subplot(2, 3, 2)
        plt.plot(x, np.sin(x), '-o')

        plt.subplot(2, 3, 3)
        plt.scatter(x, np.sin(x))

        plt.subplot(2, 3, 4)
        r = np.random.RandomState(0)
        x4 = r.randn(50)
        y4 = r.randn(50)
        colors = r.rand(50)
        sizes = 1000 * r.rand(50)
        plt.scatter(x4, y4, c=colors, s=sizes, alpha=0.3, cmap='viridis')
        plt.colorbar()

        plt.subplot(2, 3, 5)
        x5 = np.linspace(0, 10, 50)
        dy = 0.8
        y5 = np.sin(x5) + dy * np.random.randn(50)
        plt.errorbar(x5, y5, yerr=dy, fmt='.k')

        plt.subplot(2, 3, 6)
        x6 = [1, 2, 3, 4, 5, 6, 7, 8]
        y6 = [3, 1, 4, 5, 8, 9, 7, 2]
        label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        plt.barh(x6, y6, tick_label=label)

        plt.show()

    def exercise_2(self):
        '''
        1.绘制1000个随机值的直方图
        2.设置直方图分30个bins，并设置为频率分布
        3.在一张图中绘制3组不同的直方图，并设置透明度
        4.绘制一张二维直方图
        5.绘制一张设置网格大小为30的六角形直方图
        '''
        plt.subplot(2, 3, 1)
        x1 = np.random.randn(1000)
        plt.hist(x1)

        plt.subplot(2, 3, 2)
        plt.hist(x1, bins=30, histtype='stepfilled', density=True)

        plt.subplot(2, 3, 3)
        x3_1 = np.random.normal(0, 0.8, 1000)
        x3_2 = np.random.normal(-2, 1, 1000)
        x3_3 = np.random.normal(3, 2, 1000)
        opt3 = dict(alpha=0.3, bins=40, density=True)
        plt.hist(x3_1, **opt3)
        plt.hist(x3_2, **opt3)
        plt.hist(x3_3, **opt3)

        plt.subplot(2, 3, 4)
        mean = [0, 0]
        cov = [[1, 1], [1, 2]]
        x4, y4 = np.random.multivariate_normal(mean, cov, 10000).T
        plt.hist2d(x4, y4, bins=30)

        plt.subplot(2, 3, 5)
        plt.hexbin(x4, y4, gridsize=30)

        plt.show()


if __name__ == '__main__':
    print('Practice 2')
    exampleLabel = Practice2()
    # exampleLabel.exercise_1()
    exampleLabel.exercise_2()

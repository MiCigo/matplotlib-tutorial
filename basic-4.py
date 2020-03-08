'''
@Description: code
@Author: MiCi
@Date: 2020-03-08 15:58:24
@LastEditTime: 2020-03-08 20:11:27
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


class BasciLabel4(object):

    def __init__(self):
        return

    def subplot_label(self):
        # subplot划分为均匀子图， arg1、2为行、列，arg3为位置
        plt.subplot(2, 2, 1)
        plt.plot([0, 1], [0, 1])

        plt.subplot(2, 2, 2)
        plt.plot([0, 1], [0, 2])

        plt.subplot(2, 2, 3)
        plt.plot([0, 1], [0, 3])

        plt.show()

        # 不均匀子图
        plt.subplot(2, 1, 1)
        plt.plot([0, 1], [0, 1])

        plt.subplot(2, 3, 4)
        plt.plot([0, 1], [0, 2])

        plt.subplot(2, 3, 5)
        plt.plot([0, 1], [0, 4])

        plt.show()

    def grid_label(self):
        # subplot2grid以及gridspec都可以实现，有前端知识这块就很容易理解
        plt.figure(figsize=(8, 8))
        # gridspec.GridSpec将图划分为几行几列
        gs = gridspec.GridSpec(3, 3)

        ax1 = plt.subplot(gs[0, :])
        ax1.plot([0, 1], [0, 2])
        ax1.set_title('ax1 title')
        ax2 = plt.subplot(gs[1, :2])
        ax2.scatter([1, 2], [1, 2])
        ax3 = plt.subplot(gs[1:, 2])
        ax4 = plt.subplot(gs[-1, 0])
        ax5 = plt.subplot(gs[-1, -2])

        plt.show()

    def plotinplot_label(self):
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [1, 3, 4, 2, 5, 8, 6]
        # 百分比
        left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
        fig = plt.figure()
        ax1 = fig.add_axes([left, bottom, width, height])
        ax1.plot(x, y, 'r')

        # 子图画法1
        left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
        ax2 = fig.add_axes([left, bottom, width, height])
        ax2.plot(y, x, 'b')
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.set_title('inside 1')

        # 子图画法2
        plt.axes([0.6, 0.2, 0.25, 0.25])
        plt.plot(y[::-1], x, 'g')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('inside 2')

        plt.show()

    def second_axis(self):
        x = np.arange(0, 10, 0.1)
        y1 = 0.05 * x**2
        y2 = -1 * y1

        # 调用twinx使两个轴倒置
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(x, y1, 'g')
        ax1.set_xlabel('x data')
        ax1.set_ylabel('y1 data')
        ax2.plot(x, y2, 'b')
        ax2.set_ylabel('y2 data')

        plt.show()

    def basic_label_4_practice(self):
        print('write your anwser')

    def basic_label_4_practice_answer(self):
        return


if __name__ == '__main__':
    print('Start about basic label 4')
    exampleLabel = BasciLabel4()
    # subplot多合一
    # exampleLabel.subplot_label()
    # grid排列
    # exampleLabel.grid_label()
    # 图中图
    # exampleLabel.plotinplot_label()
    # 次坐标
    exampleLabel.second_axis()

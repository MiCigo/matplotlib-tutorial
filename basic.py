# -*- coding: utf-8 -*-
'''
@Description: code
@Author: MiCi
@Date: 2020-03-07 20:52:48
@LastEditTime: 2020-03-07 22:44:34
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import numpy as np


def basic_label():
    x = np.linspace(-3, 3, 50)
    y1 = x*2 + 1
    y2 = x**2
    # 图标大小
    # plt.figure(num=1, figsize=(5, 8))

    # plot画图
    plt.plot(x, y1)
    plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

    # xlim + ylim 定义坐标轴范围
    plt.xlim((-1, 2))
    plt.ylim((-2, 3))

    # xlabel + ylabel 定义坐标轴名称
    plt.xlabel('X')
    plt.ylabel('Y')

    # xticks + yticks 定义坐标轴刻度&名称
    new_ticks = np.linspace(-1, 2, 5)
    print(new_ticks)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, 1, 3], ['first', 'second', 'third', 'fourth'])

    # 设置图形边框
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    # xaxis + yaxis set_ticks_position设置坐标刻度数组或名字位置
    # 名称位置（top、bottom、both、default、none）
    ax.xaxis.set_ticks_position('bottom')
    # set_position 设定y=0的位置（outwart、axes、data）
    ax.spines['bottom'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # plot显示
    plt.show()


def basic_label_practice():
    # 基础画图练习
    x = np.linspace(-1, 2, 50)
    y = x - 1
    plt.figure()
    plt.plot(x, y, linewidth=1.0, linestyle='--')
    plt.xlim((-1, 2))
    plt.ylim((-2, 1))
    plt.xticks([-1, -0.5, 1], ['bad', 'normal', 'good'])
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    plt.show()


if __name__ == '__main__':
    print('hello world')
    basic_label()
    basic_label_practice()

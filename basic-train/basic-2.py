# -*- coding: utf-8 -*-
'''
@Description: code
@Author: MiCi
@Date: 2020-03-07 22:46:46
@LastEditTime: 2020-03-12 10:47:55
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import numpy as np


def basic_label_2():
    x = np.linspace(-3, 3, 50)
    y1 = x*2 + 1
    y2 = x**2
    # label属性设定 图例名称
    plt.plot(x, y1, label='y1 name')
    plt.plot(x, y2, color='red', linewidth=1.0,
             linestyle='--', label='y2 name')

    plt.xlim((-1, 2))
    plt.ylim((-2, 3))
    plt.xlabel('X')
    plt.ylabel('Y')
    new_ticks = np.linspace(-1, 2, 5)
    plt.xticks(new_ticks)
    plt.yticks([-2, -1.8, 1, 3], ['first', 'second', 'third', 'fourth'])

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # 绘制图例，通过loc参数设定图例位置
    #  'best': 0， 'upper right': 1, 'upper left': 2, 'lower left': 3
    # 'lower right': 4, 'right': 5, 'center left': 6, 'center right': 7
    # 'lower center': 8, 'upper center': 9, 'center': 10
    plt.legend(loc=0)

    tempx = 0.5
    tempy = 2*tempx + 1
    # 再画一条垂直线
    plt.plot([tempx, tempx, ], [0, tempy, ], 'k--', linewidth=2)
    # scatter在图中画点，设定size与color
    plt.scatter([tempx, ], [tempy, ], s=50, color='b')

    # annotate添加注释，xytext + textcoords表示对于标注的描述和偏离
    # arrowprops对图中箭头类型和箭头弧度的设置
    plt.annotate(
        '2x+1=%s' % tempy, xy=(tempx, tempy),
        xycoords='data', xytext=(+30, -30),
        textcoords='offset points', fontsize=16,
        arrowprops=dict(
            arrowstyle='->', connectionstyle='arc3,rad=.2'
        )
    )

    # text，直接通过设置注释
    plt.text(-1, 1, 'test test', fontdict={'size': 16, 'color': 'b'})

    plt.show()


def basic_label_2_practice():
    print('write your anwser')


def basic_label_2_practice_answer():
    return


if __name__ == '__main__':
    print('Start learn basic label 2')
    basic_label_2()

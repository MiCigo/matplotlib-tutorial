'''
@Description: code
@Author: MiCi
@Date: 2020-03-08 20:15:59
@LastEditTime: 2020-03-09 19:27:00
@LastEditors: MiCi
'''


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class BasciLabel5(object):

    def __init__(self):
        return

    def a3d_label(self):
        # 定义一个3D坐标轴
        fig = plt.figure()
        ax = Axes3D(fig)

        x = np.arange(-4, 4, 0.25)
        y = np.arange(-4, 4, 0.25)
        # x、y为平面网格
        x, y = np.meshgrid(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        # z为高
        z = np.sin(r)

        # rstride、cstride分别代表row和column的跨度，跨度越小，网格越密
        ax.plot_surface(x, y, z, rstride=1, cstride=1,
                        cmap=plt.get_cmap('rainbow'))

        plt.show()

    def basic_label_5_practice(self):
        print('write your anwser')

    def basic_label_5_practice_answer(self):
        return


if __name__ == '__main__':
    print('Start about basic label 5')
    exampleLabel = BasciLabel5()
    # 3D图
    exampleLabel.a3d_label()

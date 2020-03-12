'''
@Description: code
@Author: MiCi
@Date: 2020-03-08 20:15:59
@LastEditTime: 2020-03-12 10:48:03
@LastEditors: MiCi
'''


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


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

    def projection_label(self):

        fig = plt.figure()
        ax = Axes3D(fig)

        x = np.arange(-4, 4, 0.25)
        y = np.arange(-4, 4, 0.25)
        x, y = np.meshgrid(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        z = np.sin(r)

        ax.plot_surface(x, y, z, rstride=1, cstride=1,
                        cmap=plt.get_cmap('rainbow'))
        # zdir选择投影轴，调整offset为调整投影位置
        # ax.contourf(x, y, z, zdir='z', offset=-1,
        #               cmap=plt.get_cmap('rainbow'))
        ax.contourf(x, y, z, zdir='x', offset=-4, cmap=plt.get_cmap('rainbow'))

        plt.show()

    def animation_label(self):
        fig, ax = plt.subplots()
        x = np.arange(0, 2*np.pi, 0.01)
        line, = ax.plot(x, np.sin(x))

        def animate(i):
            line.set_ydata(np.sin(x + i/10.0))
            return line,

        def ani_init():
            line.set_ydata(np.sin(x))
            return line,

        # fig进行动画绘制的figure图，func自定义动画函数
        # frames 动画长度一次循环的帧数， init_func自定义开始帧
        # interval 更新频率，单位ms
        # blit 选择更新所有点，对mac兼容有问题，使用false
        ani = animation.FuncAnimation(fig=fig,
                                      func=animate,
                                      frames=100,
                                      init_func=ani_init,
                                      interval=20,
                                      blit=True)
        plt.show()

    def basic_label_5_practice(self):
        print('write your anwser')

    def basic_label_5_practice_answer(self):
        return


if __name__ == '__main__':
    print('Start learn basic label 5')
    exampleLabel = BasciLabel5()
    # 3D图
    # exampleLabel.a3d_label()
    # 投影
    # exampleLabel.projection_label()
    # 动画
    exampleLabel.animation_label()

'''
@Description: code
@Author: MiCi
@Date: 2020-03-07 23:38:05
@LastEditTime: 2020-03-12 10:47:47
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import numpy as np


class BasciLabel3(object):

    def __init__(self):
        return

    def scatter_label(self):
        n = 512
        x = np.random.normal(0, 1, n)
        y = np.random.normal(0, 1, n)
        t = np.arctan2(y, x)

        # 画点集，size:50 color取t，alpha为50%透明度
        plt.scatter(x, y, s=50, c=t, alpha=.5)

        plt.xlim(-1.5, 1.5)
        plt.ylim(-1.5, 1.5)

        # xticks传入空集隐藏坐标轴
        plt.xticks(())
        plt.yticks(())

        plt.show()

    def bar_label(self):
        n = 12
        x1 = np.arange(n)
        y1 = (1 - x1 / float(n)) * np.random.uniform(0.5, 1.0, n)
        y2 = (1 - x1/float(n)) * np.random.uniform(0.5, 1.0, n)

        # facecolor设置柱状图主题颜色，edgecolor设置边框颜色
        plt.bar(x1, +y1, facecolor='#FFCCCC', edgecolor='black')
        plt.bar(x1, -y2, facecolor='#6699CC', edgecolor='white')

        # text 在柱体上下方加上数值，ha='center'横向居中，va='bottom'纵向底部对齐
        for x, y in zip(x1, y1):
            plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
        for x, y in zip(x1, y2):
            plt.text(x, -y, '%.2f' % y, ha='center', va='top')

        plt.show()

    def height_create(self, x, y):
        return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

    def height_label(self):
        n = 256
        x = np.linspace(-3, 3, n)
        y = np.linspace(-3, 3, n)
        x1, y1 = np.meshgrid(x, y)

        # contourf把颜色填入，arg1、2、3：位置参数1，arg4为密集程度
        # alpha设定透明度，cmap设定颜色映射关系
        # https://matplotlib.org/examples/color/colormaps_reference.html
        plt.contourf(x1, y1, self.height_create(x1, y1),
                     8, alpha=.75, cmap=plt.cm.RdBu)

        # 使用contour函数画线
        C = plt.contour(x1, y1, self.height_create(x1, y1),
                        8, colors='black', linewidth=.5)

        # 使用clabel添加高度数值，inline决定是否写入线中
        plt.clabel(C, inline=True, fontsize=10)
        plt.xticks(())
        plt.yticks(())

        plt.show()

    def random_matrix_label(self):
        a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
                      0.365348418405, 0.439599930621, 0.525083754405,
                      0.423733120134, 0.525083754405, 0.651536351379]
                     ).reshape(3, 3)
        # 使用imshow绘图，origin代表原点位置，interpolation表示画图方式
        # https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
        plt.imshow(a, interpolation='nearest', cmap='RdBu', origin='lower')

        # colorbar添加颜色条,shrink参数调整长度
        plt.colorbar(shrink=.92)

        plt.show()

    def basic_label_3_practice(self):
        print('write your anwser')

    def basic_label_3_practice_answer(self):
        return


if __name__ == '__main__':
    print('Start learn basic label 3')
    exampleLabel = BasciLabel3()
    # 散点图
    # exampleLabel.scatter_label()
    # 柱状图
    # exampleLabel.bar_label()
    # 等高线图
    # exampleLabel.height_label()
    # 随机矩阵图
    exampleLabel.random_matrix_label()

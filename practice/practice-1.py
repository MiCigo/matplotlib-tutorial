'''
@Description: code
@Author: MiCi
@Date: 2020-03-09 20:20:16
@LastEditTime: 2020-03-10 14:32:04
@LastEditors: MiCi
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from mpl_toolkits.mplot3d import Axes3D


class Practice1(object):

    def __init__(self):
        return

    def exercise_1(self):
        '''
        在实际的数据分析过程中，我们往往需要对一个表格中的多个项目进行比较分析
        这个时候，组合柱状图就派上了用场。通过第三章所学的知识，你能否将下表数据用组合柱状图的形式呈现？
        其中，横坐标为水果种类，纵坐标为价格与数量。 提示：进行两次画图操作，注意计算好柱形图的x轴位置
        水果	价格	数量
        香蕉	2	5
        苹果	4	3
        草莓	10	6
        '''
        raw_data = {'水果': ['香蕉', '苹果', '草莓'],
                    '价格': [2, 4, 10],
                    '数量': [5, 3, 6], }
        df = pd.DataFrame(raw_data)

        pos = list(range(len(df['水果'])))
        width = 0.25
        plt.bar([p - width/2 for p in pos], df['价格'],
                width, color='#FFCCCC', label=df['水果'][0])
        plt.bar([p + width/2 for p in pos], df['数量'],
                width, color='#6699CC', label=df['水果'][1])
        plt.xticks(np.linspace(0, 2, 3), df['水果'])
        plt.legend(['价格', '数量'], loc='upper left')
        plt.show()

    def exercise_2(self):
        '''
        “人力资源分析数据集”（/data/HR_comma_sep.csv），数据集中的字段包括：
        对环境的满意度(satisfaction_level)
        每月加班平均时间(average_montly_hours) 对现有的项目的满意度(last_evaluation)
        请你利用散点图挖掘出员工对环境满意度和其每月加班平均时间的关系
        '''
        HR_data = pd.read_csv('.\data\HR_comma_sep.csv')
        HR_data.shape
        # HR_data.head()
        data = shuffle(HR_data).iloc[:200, :]
        x = data['average_montly_hours'].tolist()
        y = data['satisfaction_level'].tolist()
        t = np.arctan2(y, x)
        plt.scatter(x, y, c=t)
        plt.xlabel('hours')
        plt.ylabel('satisfaction level')
        plt.show()

    def exercise_3(self):
        '''
        针对“人力资源分析数据集”，挖掘对现有的项目的满意度和月平均加班时间之间的关系；并将此图和上图合并显示
        '''
        HR_data = pd.read_csv('.\data\HR_comma_sep.csv')
        HR_data.shape

        data = shuffle(HR_data).iloc[:200, :]
        x = data['average_montly_hours'].tolist()
        y1 = data['satisfaction_level'].tolist()
        y2 = data['last_evaluation'].tolist()
        t1 = np.arctan2(y1, x)
        t2 = np.arctan2(y2, x)

        plt.figure(figsize=(12, 8))

        plt.subplot(1, 2, 1)
        plt.scatter(x, y1, c=t1)
        plt.xlabel('hours')
        plt.ylabel('satisfaction_level')

        plt.subplot(1, 2, 2)
        plt.scatter(x, y2, c=t2)
        plt.xlabel('hours')
        plt.ylabel('last_evaluation')

        plt.show()

    def exercise_4(self):
        '''
        请在3D坐标系下画出函数Z=3 (1-X)**2 np.e(-(X2) - (Y+1)2)- 
        10*(X/5 - X3 - Y5)*np.e(-X2-Y2)- 1/3*np.e(-(X+1)2 - Y**2);
        并将其投影至 x=-4 和 z=-7 平面上;并添加colorbar
        '''
        X = np.arange(-4, 4, 0.25)
        Y = np.arange(-4, 4, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = 3 * (1-X)**2 * np.e**(-(X**2) - (Y+1)**2) - \
            10*(X/5 - X**3 - Y**5)*np.e**(-X**2-Y**2) - \
            1/3*np.e**(-(X+1)**2 - Y**2)
        fig = plt.figure(figsize=(10, 6))
        ax = Axes3D(fig)
        cmap = 'Spectral'
        m = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                            cmap=plt.get_cmap(cmap))
        ax.contourf(X, Y, Z, zdir='x', offset=-4)
        ax.contourf(X, Y, Z, zdir='z', offset=-7)
        plt.colorbar(m, shrink=0.6)
        plt.show()


if __name__ == '__main__':
    print('Practice 1')
    exampleLabel = Practice1()
    # exampleLabel.exercise_1()
    # exampleLabel.exercise_2()
    # exampleLabel.exercise_3()
    exampleLabel.exercise_4()

from cProfile import label
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np

class PyDisps:
    plt.rcParams['font.sans-serif']=['SimHei'] #指定分辨率
    plt.rcParams['axes.unicode_minus'] = False
    def __init__(self,datas,bins,xleft,xright,label):
        self.datas = datas #数据集[, ,]
        self.bins = bins #设置连续的边界值，即直方图的分布区间[0,10]
        self.xleft = xleft #x轴左边界
        self.xright = xright#x轴右边界
        self.label = label#标签

    def frequent_distribution(self):
        n, bins, patches = plt.hist(self.datas,self.bins,range=(self.xleft,self.xright),color='b', alpha=0.3, label=self.label, histtype='stepfilled')#alpha设置透明度
        print("每个柱子内的个数: ",n)
        print("每个柱的区间范围: ",bins)
        plt.legend(loc='upper right') #图例在右上角
        plt.grid(True, ls=':') #设置网格线
        plt.xlabel('X')
        plt.ylabel('y')
        plt.show()

if __name__ == '__main__':
    br = input("请输入随机数产生的范围(用,隔开):")
    xleft = eval(br.split(',')[0])
    xright = eval(br.split(',')[1])
    bins = xright - xleft
    datas=np.random.randint(xleft,xright,100)#生成【0-100】之间的100个数据,即 数据集
    d1=PyDisps(datas,bins,xleft,xright,u"均匀分布")
    d1.frequent_distribution()
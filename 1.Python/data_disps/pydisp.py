# coding=gbk
from cProfile import label
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np

class PyDisps:

    plt.rcParams['font.sans-serif']=['SimHei'] #指定分辨率
    plt.rcParams['axes.unicode_minus'] = False
    def __init__(self,bins,xleft,xright):
        # self.datas = datas #数据集[, ,]
        self.bins = bins #设置连续的边界值，即直方图的分布区间[0,10]
        self.xleft = xleft #x轴左边界
        self.xright = xright#x轴右边界
        # self.label = label#标签


    def frequent_distribution(self,datas):
        n, bins_num, patches = plt.hist(datas,self.bins,range=(self.xleft,self.xright),color='b', alpha=0.5, histtype='bar',edgecolor="r")#alpha设置透明度
        plt.plot(bins_num[:self.bins],n,marker = 'o',color="r",linestyle="--")
        print("每个柱子内的个数: ",n)
        print("每个柱的区间范围: ",bins)
        plt.title("data analyze")
        plt.legend(loc='upper right') #图例在右上角
        plt.grid(True, ls=':') #设置网格线
        plt.xlabel('height')
        plt.ylabel('rate')
        plt.show()
    
    def rd_data2list(self,filelocal):
        pos = []
        with open(filelocal, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline() 
                lines = lines.strip('\n')
                if not lines:
                    break
                so = int(lines) / (2**32-1)
                rd = self.xleft + int((self.xright-self.xleft)*so)
                pos.append(rd)
        # cnt = pos.len()
        return pos 

if __name__ == '__main__':
    br = input("请输入随机数产生的范围(用,隔开):")
    xleft = eval(br.split(',')[0])
    xright = eval(br.split(',')[1])
    bins = xright - xleft
    datas=np.random.randint(xleft,xright,100000)#生成【0-100】之间的100个数据,即 数据集
    d1=PyDisps(bins,xleft,xright)
    # datas = d1.rd_data2list("E:\\ZYNQ-Source\\2.axis_mt19937\\tdata.txt")
    d1.frequent_distribution(datas)
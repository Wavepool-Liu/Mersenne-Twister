# coding=gbk
from cProfile import label
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np

class PyDisps:

    plt.rcParams['font.sans-serif']=['SimHei'] #ָ���ֱ���
    plt.rcParams['axes.unicode_minus'] = False
    def __init__(self,bins,xleft,xright):
        # self.datas = datas #���ݼ�[, ,]
        self.bins = bins #���������ı߽�ֵ����ֱ��ͼ�ķֲ�����[0,10]
        self.xleft = xleft #x����߽�
        self.xright = xright#x���ұ߽�
        # self.label = label#��ǩ


    def frequent_distribution(self,datas):
        n, bins_num, patches = plt.hist(datas,self.bins,range=(self.xleft,self.xright),color='b', alpha=0.5, histtype='bar',edgecolor="r")#alpha����͸����
        plt.plot(bins_num[:self.bins],n,marker = 'o',color="r",linestyle="--")
        print("ÿ�������ڵĸ���: ",n)
        print("ÿ���������䷶Χ: ",bins)
        plt.title("data analyze")
        plt.legend(loc='upper right') #ͼ�������Ͻ�
        plt.grid(True, ls=':') #����������
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
    br = input("����������������ķ�Χ(��,����):")
    xleft = eval(br.split(',')[0])
    xright = eval(br.split(',')[1])
    bins = xright - xleft
    datas=np.random.randint(xleft,xright,100000)#���ɡ�0-100��֮���100������,�� ���ݼ�
    d1=PyDisps(bins,xleft,xright)
    # datas = d1.rd_data2list("E:\\ZYNQ-Source\\2.axis_mt19937\\tdata.txt")
    d1.frequent_distribution(datas)
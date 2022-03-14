#梅森旋转算法
#参考:mersenne twister from wikipedia
from time import time
from data_disps import pydisp
#MT19937-32的参数列表如下
W,N,M,R = 32,624,397,31 #长度，递归长度，周期参数，低位掩码
A,F = 0X9908B0DF,1812433253#旋转矩阵的参数，初始化梅森旋转链所需参数
U,D,L = 11,0XFFFFFFFF,18#额外梅森旋转所需的掩码和位移量
C,B = 4022730752 ,2636928640 #TGFSR的掩码
T,S = 15,7 #TGFSR的位移量

#初始化索引和旋转链
index = 0
MT = [0]*N 

def inter(t):   
    #取最后32位->t
    return(0xFFFFFFFF & t) 

def twister(): 
    #用旋转算法处理旋转链
    global index,N,A
    for i in range(N):
        y = inter((MT[i] & 0x80000000) +(MT[(i + 1) % N] & 0x7fffffff)) # （MT[i]&0x8000000）取高(W-R)位和(MT[i+1]&0x7fffffff)取低R位连接;mod是为了MT[623]和MT[0]再进行一次旋转
        MT[i] = MT[(i + 397) % N] ^ y >> 1  # y与MT[i+m]异或,再右移一位
        if y % 2 != 0: #若最低位为1，则与a（旋转矩阵的参数）异或
            MT[i] = MT[i] ^ A
    index = 0

def exnum():
    #对旋转算法所得结果进行处理
    global index,U,D,S,B,T,C,L,N
    if index >= N or index == 0: #每输出n个数字要执行一次旋转算法，以保证随机性
        twister() #旋转算法
    y = MT[index]
    y = y ^ y >> U & D
    y = y ^ y << S & B
    y = y ^ y << T & C
    y = y ^ y >> L
    index = index + 1 # 如果重复获取，这个index就能在MT[0]~MT[623]获取623次之后重新再更新旋转链
    return inter(y)

def mainset(seed): 
    #初始化MT[],获得基础梅森旋转链
    global F,W,N
    MT[0] = seed    #seed
    for i in range(1,N): #一共623次，因为MT[0]已经放入seed
        MT[i] = inter(F * (MT[i - 1] ^ MT[i - 1] >> (W-2)) + i) # >>30=(w-2)；f = 1812433253
    return exnum()

def main(times,xleft,xright):
    datas = [0]*times
    for i in range(times):#输出times个随机数
        so = mainset(int(time())) / (2**32-1)#利用time()输入seed种子，输入到mainset中获得[0,2^w -1]范围内的离散型均匀分布随机数
        rd = xleft + int((xright-xleft)*so)
        datas[i] = rd
    return datas

if __name__ == '__main__':
    TIMES = 200000 #输出个数
    while True:
        br = input("请输入随机数产生的范围(用,隔开):")
        xleft = eval(br.split(',')[0])
        xright = eval(br.split(',')[1])
        datas = main(TIMES,xleft,xright)
        d1 = pydisp.PyDisps(datas,xright-xleft,xleft,xright,u'均匀分布')
        d1.frequent_distribution()
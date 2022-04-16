# coding=gbk
#÷ɭ��ת�㷨
#�ο�:mersenne twister from wikipedia

from time import time
from data_disps import pydisp
#MT19937-32�Ĳ����б�����
W,N,M,R = 32,624,397,31 #���ȣ��ݹ鳤�ȣ����ڲ�������λ����
A,F = 0X9908B0DF,1812433253#��ת����Ĳ�������ʼ��÷ɭ��ת���������
U,D,L = 11,0XFFFFFFFF,18#����÷ɭ��ת����������λ����
C,B = 4022730752 ,2636928640 #TGFSR������
T,S = 15,7 #TGFSR��λ����

#��ʼ����������ת��
index = 0
MT = [0]*N 

def inter(t):   
    #ȡ���32λ->t
    return(0xFFFFFFFF & t) 

def twister(): 
    #����ת�㷨������ת��
    global index,N,A
    for i in range(N):
        y = inter((MT[i] & 0x80000000) +(MT[(i + 1) % N] & 0x7fffffff)) # ��MT[i]&0x8000000��ȡ��(W-R)λ��(MT[i+1]&0x7fffffff)ȡ��Rλ����;mod��Ϊ��MT[623]��MT[0]�ٽ���һ����ת
        # MT[i] = MT[(i + 397) % N] ^ y >> 1  # y��MT[i+m]���,������һλ
        MT[i] = MT[(i + 87) % N] ^ MT[(i + 148) % N] ^ MT[(i + 241) % N] ^ y >> 1  # y��MT[i+m]���,������һλ
        if y % 2 != 0: #�����λΪ1������a����ת����Ĳ��������
            MT[i] = MT[i] ^ A
    index = 0

def exnum():
    #����ת�㷨���ý�����д���
    global index,U,D,S,B,T,C,L,N
    if index >= N or index == 0: #ÿ���n������Ҫִ��һ����ת�㷨���Ա�֤�����
        twister() #��ת�㷨
    y = MT[index]
    y = y ^ y >> U & D
    y = y ^ y << S & B
    y = y ^ y << T & C
    y = y ^ y >> L
    index = index + 1 # ����ظ���ȡ�����index������MT[0]~MT[623]��ȡ623��֮�������ٸ�����ת��
    return inter(y)

def mainset(seed): 
    #��ʼ��MT[],��û���÷ɭ��ת��
    global F,W,N
    MT[0] = seed    #seed
    for i in range(1,N): #һ��623�Σ���ΪMT[0]�Ѿ�����seed
        MT[i] = inter(F * (MT[i - 1] ^ MT[i - 1] >> (W-2)) + i) # >>30=(w-2)��f = 1812433253
    return exnum()

def main(times,xleft,xright):
    datas = [0]*times
    for i in range(times):#���times�������
        so = mainset(int(time()))#����time()����seed���ӣ����뵽mainset�л��[0,2^w -1]��Χ�ڵ���ɢ�;��ȷֲ������
        print(so)
        so = so / (2**32-1)
        rd = xleft + int((xright-xleft)*so)
        datas[i] = rd
        # print(datas)
    return datas

if __name__ == '__main__':
    TIMES = 100000 #�������
    while True:
        br = input("����������������ķ�Χ(��,����):")
        xleft = eval(br.split(',')[0])
        xright = eval(br.split(',')[1])
        datas = main(TIMES,xleft,xright)
        d1 = pydisp.PyDisps(xright-xleft,xleft,xright,u'���ȷֲ�')
        d1.frequent_distribution(datas)
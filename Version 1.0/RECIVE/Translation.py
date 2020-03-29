from RECIVE.Decode import Decode
from RECIVE.color import Color
import cv2
import numpy as np
import os
import time
from SENDCODE.Parameter import par
import struct
# 引入time模块

def BIN_TO_CHAR(str):
    str='0b'+str
    return int(str, 2)

def Exchange(Data):
    L = len(Data)#1920
    K = int(L/8)
    Data_temp=[]
    step=8
    index=0
    for i in range(K):
        Data_temp.append(BIN_TO_CHAR(Data[index:index+step]))
        index+=step
    return Data_temp

def Translation(path):
    image_list = os.listdir(path)
    Data=[]
    # print(image_list)
    ticks = time.time()
    Var=[]
    for picture in image_list:
        Data_temp, Var_z = Decode(path+'\\'+picture)
        Data += Exchange(Data_temp)
        Var +=Exchange(Var_z)
    ticks2 = time.time()
    ticks = ticks2-ticks
    return Data, ticks, Var

if __name__=='__main__':
    # Translation('E:\Generation\Last\Picture_cap')
    ticks = time.time()
    path = 'E:\Generation\Last\Picture_cap'
    a,b, c = Translation(path)
    for i in a:
        print(i)
        # print(i.encode('ascii'))
    ticks2 = time.time()
    print(ticks2-ticks)
    # 前面省略，从下面直奔主题，举个代码例子：
    result2txt =a  # data是前面运行出的数据，先将其转为字符串才能写入
    # with open('结果存放.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
    #     file_handle.write(result2txt)  # 写入
    #     file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
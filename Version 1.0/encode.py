from SENDCODE.Coding import Code
from SENDCODE.GEN_video import Gen_Video
from SENDCODE.Parameter import par
import os
import struct

Par = par()
Lengh = Par.Lengh
Width = Par.Width
Point_size = Par.Point_size#点的宽度
D_size = Par.D_size#定位点像素宽度
Data_L = Par.Data_L
Dara_H = Par.Data_H
T = int(Par.Total/4)

def Read(Time,kps, path):
    k = (T*Time*kps)/1000
    k = int(k)
    Data = []
    binfile = open(path, 'rb')
    for i in range(k):
        data = binfile.read(1)
        num = struct.unpack('B', data)
        Data.append(num[0])
    return Data




def Send_main(kps, Time, video_name, filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + '\Picture'
    file = current_dir+'\BIN\\'+filename
    video_name = current_dir +'\Send_video\\'+video_name+'.avi'
    Data = Read(kps,Time,file)
    count = Code(Data, 0, path)
    Gen_Video(path,video_name, kps)
    return count

if __name__=='__main__':
    Send_main(10, 8000, 'e5', 'e5.bin')
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # print(current_dir)
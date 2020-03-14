from SENDER_CODE.Coding import Code
from SENDER_CODE.GEN_video import Gen_Video
import os

def Read(Time,kps, path):
    k = (3*Time*kps)/25
    k = int(k)
    Data = ''
    with open(path, "rb") as file:
        Data += file.read().decode('ascii')
    return Data[0:k]

def Send_main(kps, Time, video_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = current_dir + '\Picture'
    file = current_dir+'\BIN\in.bin'
    video_name = current_dir +'\Send_video\\'+video_name+'.avi'
    Data = Read(kps,Time,file)
    count = Code(Data, 0, path)
    Gen_Video(path,video_name, kps)
    return count

if __name__=='__main__':
    # Send_main(10, 1000, 'asd'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)
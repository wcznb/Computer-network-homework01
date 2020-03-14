from REC_CODE.Translation import Translation
from REC_CODE.Cap import capture
import os

def Receive_main(vied_name, frameFrequency, save_file):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    vied_name = current_dir+'\Video\\'+vied_name
    # save_picture = current_dir+"\Picture_cap\\"
    save_picture = './Picture_cap/'
    # capture(vied_name, frameFrequency, save_picture)
    path = current_dir+'\Picture_cap'
    result2txt=Translation(path)
    with open('结果存放.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(result2txt)  # 写入
        file_handle.write('\n')
if __name__=='__main__':
    Receive_main('out.mp4',1,0)
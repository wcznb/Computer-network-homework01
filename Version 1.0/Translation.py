from REC_CODE.Decode import Decode
from REC_CODE.color import Color
import cv2
import numpy as np
import os
import time
# 引入time模块


wordvect = {
            '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09',
            'a': '10', 'b': '11', 'c': '12', 'd': '13', 'e': '14', 'f': '15', 'g': '16',
            'h': '17', 'i': '18', 'j': '19', 'k': '20', 'l': '21', 'm': '22', 'n': '23',
            'o': '24', 'p': '25', 'q': '26', 'r': '27', 's': '28', 't': '29', 'u': '30',
            'v': '31', 'w': '32', 'x': '33', 'y': '34', 'z': '35',
            'A': '36', 'B': '37', 'C': '38', 'D': '39', 'E': '40', 'F': '41', 'G': '42',
            'H': '43', 'I': '44', 'J': '45', 'K': '46', 'L': '47', 'M': '48', 'N': '49',
            'O': '50', 'P': '51', 'Q': '52', 'R': '53', 'S': '54', 'T': '55', 'U': '56',
            'V': '57', 'W': '58', 'X': '59', 'Y': '60', 'Z': '61',
            '': '62', ' ': '63', '\n': '64', '0':'65'
}

vectword = dict(zip(wordvect.values(), wordvect.keys()))
# print(vectword)

#过滤图片#待改进by找好过滤颜色的范围
def Picture_list(path):
    List_temp=[]
    qrcode = cv2.QRCodeDetector()
    pictures = os.listdir(path)
    print(pictures)
    before = ''
    for picture in pictures:
        image = cv2.imread(path+'\\'+picture)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        D = qrcode.detect(img_gray)
        if(D[0]==False): continue
        D = np.squeeze(D[1])
        x = int(D[2][0])
        y = int(D[2][1])
        image = image[y-30:y+10,x-30:x+10]
        clor = Color(image)
        # print(clor)
        # cv2.namedWindow('Mask_dilate', 0)
        # cv2.imshow('Mask_dilate', image)
        # cv2.waitKey()
        if(clor!=before):
            List_temp.append(picture)
            before=clor
    return List_temp

def Exchange(Data):
    L = len(Data)
    K = int(L/2)
    Data_temp=''
    for i in range(K):
        index=i*2
        S = str(Data[index:index+2])
        if(S in vectword.keys()):
            Data_temp+=vectword[S]
    return Data_temp
def Translation(path):
    # image_list = Picture_list(path)
    image_list = os.listdir(path)
    Data=''
    for picture in image_list:
        print(picture)
        Data += Exchange(Decode(path+'\\'+picture))
        # Data +=Decode(path+'\\'+picture)
    return Data

if __name__ =='__main__':
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    ticks = time.time()
    path = "E:\Generation\MY\Picture_cap"
    a = Translation(path)
    ticks2 = time.time()
    print(ticks2-ticks)
    # 前面省略，从下面直奔主题，举个代码例子：
    result2txt =a  # data是前面运行出的数据，先将其转为字符串才能写入
    with open('结果存放.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(result2txt)  # 写入
        file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据



import cv2
import numpy as np
import os
from REC_CODE.color import Color

def filter(image, D):
    x = int((D[1][0]+D[0][0])/2)
    y = int((D[1][1]+D[0][1])/2)
    image = image[y - 15:y + 15, x - 15:x + 15]
    clor = Color(image)
    return clor

def capture(path,current_path):
    vc = cv2.VideoCapture(current_path+'/Video/'+path)
    count = 1
    qrcode = cv2.QRCodeDetector()
    before=''
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        rval, frame = vc.read()
        if(np.all(frame==None)):continue
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        D = qrcode.detect(img_gray)
        if(D[0]==False):continue
        D = np.squeeze(D[1])
        x = int(D[2][0])
        y = int(D[2][1])
        if(x*y<=0):continue
        col = filter(frame, D)
        if(before==col):continue
        before = col
        name = '0000' + str(count)
        name = name[len(name) - 4:]
        print(name,frame.shape,before)
        cv2.imwrite(current_path+'/Picture_cap/' + str(name) + '.png', frame)
        count = count + 1
        cv2.waitKey(1)
    vc.release()



if __name__ == '__main__':
    capture('out2.mp4','E:\Generation\MY')
    # a = Picture_list('./Picture_cap')
    # a = Picture_list('./Picture_cap')
    # print(a)
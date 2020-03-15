import cv2
import numpy as np
import os
import time

CODE = {'0': ['red', 'green'], '1': ['red', 'blue'], '2': ['red', 'yellow'], '3': ['green', 'red'],
        '4': ['green', 'blue'], '5': ['green', 'yellow'], '6': ['blue', 'red'], '7': ['blue', 'green'],
        '8': ['blue', 'yellow'], '9': ['yellow', 'red']
        }

DECODE = {('red', 'green'): '0', ('red', 'blue'): '1', ('red', 'yellow'): '2', ('green', 'red'):'3',
          ('green', 'blue'): '4', ('green', 'yellow'): '5', ('blue', 'red'): '6', ('blue', 'green'): '7',
          ('blue', 'yellow'): '8', ('yellow', 'red'): '9'
          }

lower_red = np.array([160, 60, 60])
upper_red = np.array([180, 255, 255])

lower_red2 = np.array([0, 60, 60])
upper_red2 = np.array([10, 255, 255])

lower_yellow = np.array([10, 100, 100])
upper_yellow = np.array([45, 255, 255])

lower_blue = np.array([55,196,147])
upper_blue = np.array([135,255,255])

lower_green = np.array([43, 43, 46])
upper_green = np.array([98, 255, 255])

lower_white = np.array([0,0,133])
upper_white = np.array([110, 10, 255])

#颜色过滤
def filter(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # mask = cv2.dilate(mask, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # mask = cv2.erode(mask, kernel, iterations=1)
    # cv2.namedWindow('Mask_dilate', 0)
    # cv2.imshow('Mask_dilate', mask)
    # cv2.waitKey()
    # res = cv2.bitwise_and(image, image, mask=mask)
    #
    # cv2.namedWindow('res', 0)
    # cv2.imshow('res', res)
    # cv2.waitKey()
    return mask
def filter_map(total):
    return filter(total[0], total[1],total[2])

def Mask_mean(mask):
    return np.mean(mask,axis=0)

#仿射变换
def Radiological_changes(image, src):
    h, w = image.shape[:2]
    dst = np.array([[10, 10], [800, 10], [10, 800]], np.float32)
    A1 = cv2.getAffineTransform(src, dst)
    d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)
    return d1

#切割大图片
def picture_process(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qrcode = cv2.QRCodeDetector()
    a=qrcode.detect(img_gray)
    src = np.squeeze(a[1])
    src = np.delete(src, 2, 0)
    img_gray = Radiological_changes(image, src)
    image = img_gray[10:800,10:800]
    # cv2.imshow('Mask_dilate', image)
    # cv2.waitKey()
    return image

#色彩增强
def Enhance(image):
    pass

#确定输入数据的颜色列表
def Locate_color(masks):
    steps = 30
    r = list(masks[0])
    y = list(masks[1])
    b = list(masks[2])
    g = list(masks[3])
    colors=[]
    color_temp = []
    for i in range(26):
        index = i*steps
        r_count = sum(r[index:index + steps])
        y_count = sum(y[index:index + steps])
        b_count = sum(b[index:index + steps])
        g_count = sum(g[index:index + steps])
        switch = max(r_count, y_count, b_count, g_count)
        # if (switch == 0): continue
        if (i == 12): continue
        if (i == 13): continue
        if (switch == r_count):
            color_temp.append('red')
        elif (switch == y_count):
            color_temp.append('yellow')
        elif (switch == b_count):
            color_temp.append('blue')
        else:
            color_temp.append('green')
        if(i%2==1):
            z = (color_temp[0],color_temp[1])
            colors.append(z)
            color_temp=[]
    return colors

#识别一行颜色并解码
def Decode_one(image):
    lower = [lower_red, lower_red2, lower_yellow, lower_blue, lower_green]
    upper = [upper_red, upper_red2, upper_yellow, upper_blue, upper_green]
    images = [image]*5

    Data_list = list(zip(images, lower, upper))
    masks = list(map(filter_map, Data_list))
    Z = masks.pop(0)
    masks[0]+=Z
    masks = list(map(Mask_mean, masks))
    # print(len(masks))
    colors = Locate_color(masks)
    Data=''
    # print(colors)
    for color in colors:
        if(color in DECODE.keys()):
            Data+=DECODE[color]
    return Data

def Cutting_picture(image):
    # print(image.shape)
    image = image[80:710]
    pictures=[]
    step=30
    for i in range(21):
        index = i*step
        if(i==10): continue
        img = image[index+10:index+20]
        # cv2.imshow('Mask_dilate', img)
        # cv2.waitKey()
        pictures.append(img)
    return pictures


def Decode(path):
    # time1 = time.time()
    img = cv2.imread(path)
    img = picture_process(img)
    # cv2.imwrite('test1.png', img)
    pictures = Cutting_picture(img)
    Data=''
    for picture in pictures:
        Data+=Decode_one(picture)
    time2 = time.time()
    # print('总共耗时：' + str(time2 - time1) + 's')
    return Data

if __name__=="__main__":
    # ticks = time.time()
    data = Decode('aa.jpg')
    # image = cv2.imread('test.png')
    print(data)
#914149841140985214089524564987897904564132131564654654655621498615252976798793145867981589132132565698798498451481231564657981075120231084189711078360478910249857120498712048971092457830435894654312065480894418986487086917843407038
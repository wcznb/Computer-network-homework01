import cv2
import numpy as np
import time
from SENDCODE.Parameter import par

Par = par()
Lengh = Par.Lengh#
Width = Par.Width#
Point_size = Par.Point_size#
D_size = Par.D_size#
Data_L = Par.Data_L#
Data_H = Par.Data_H+Par.Data_H2#
DECODE = Par.DECODE


# lower_red = np.array([160, 60, 60])
# upper_red = np.array([180, 255, 255])
#
# lower_red2 = np.array([0, 60, 60])
# upper_red2 = np.array([10, 255, 255])
#
# lower_yellow = np.array([10, 100, 100])
# upper_yellow = np.array([45, 255, 255])
#
# lower_blue = np.array([55,196,147])
# upper_blue = np.array([135,255,255])
#
# lower_green = np.array([43, 43, 46])
# upper_green = np.array([98, 255, 255])
#
# lower_white = np.array([0,0,221])
# upper_white = np.array([180, 30, 255])
lower_red = np.array([156, 43, 46])
upper_red = np.array([180, 255, 255])

lower_red2 = np.array([0, 43, 46])
upper_red2 = np.array([10, 255, 255])

# lower_yellow = np.array([26, 43, 46])
# upper_yellow = np.array([34, 255, 255])
# lower_yellow = np.array([11, 43, 46])
# upper_yellow = np.array([43, 255, 255])


lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

# lower_green = np.array([40, 43, 46])
# upper_green = np.array([77, 255, 255])

lower_yellow = np.array([11, 43, 46])
upper_yellow = np.array([34, 255, 255])

lower_green = np.array([39, 43, 46])
upper_green = np.array([77, 255, 255])

#颜色过滤
def filter(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return mask

def filter_map(total):
    return filter(total[0], total[1],total[2])

def Mask_mean(mask):
    return np.mean(mask,axis=0)

#仿射变换
def Radiological_changes(image, src):
    h, w = image.shape[:2]
    dst = np.array([[D_size, D_size], [Lengh-D_size, D_size], [D_size, Lengh-D_size]], np.float32)
    A1 = cv2.getAffineTransform(src, dst)
    d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)
    # cv2.imshow('Mask_dilate', d1)
    # cv2.waitKey()
    return d1

#切割大图片
def picture_process(image):

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qrcode = cv2.QRCodeDetector()
    a=qrcode.detect(img_gray)
    src = np.squeeze(a[1])
    src = np.delete(src, 2, 0)
    img_gray = Radiological_changes(image, src)
    image = img_gray[0:Width-D_size,D_size:Lengh-D_size]
    return image

def Cutting_picture(image):
    pictures=[]
    step=Point_size
    index=0
    for i in range(Par.Data_H2):
        img = image[index+10:index+20,168:]
        index +=step
        pictures.append(img)

    for i in range(Par.Data_H):
        img = image[index+10:index+20]
        index +=step
        pictures.append(img)
    return pictures

#确定输入数据的颜色列表
def Locate_color(masks,L):
    steps = Point_size
    r = list(masks[0])
    y = list(masks[1])
    b = list(masks[2])
    g = list(masks[3])
    colors=[]
    color_temp = []
    for i in range(L):
        index = i*steps
        r_count = sum(r[index:index + steps])
        y_count = sum(y[index:index + steps])
        b_count = sum(b[index:index + steps])
        g_count = sum(g[index:index + steps])
        switch = max(r_count, y_count, b_count, g_count)
        # if (switch == 0): continue
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
def Decode_one(image,L):
    Var=''
    lower = [lower_red, lower_red2, lower_yellow, lower_blue, lower_green]
    upper = [upper_red, upper_red2, upper_yellow, upper_blue, upper_green]
    images = [image]*5

    Data_list = list(zip(images, lower, upper))
    masks = list(map(filter_map, Data_list))
    Z = masks.pop(0)
    masks[0]+=Z
    masks = list(map(Mask_mean, masks))
    colors = Locate_color(masks,L)
    Data=''
    # print(colors)
    for color in colors:
        if(color in DECODE.keys()):
            Data+=DECODE[color]
            Var+='1111'
        else:
            Data+='0000'
            Var+='0000'
    return Data, Var

def Decode(path):
    Var=''
    # time1 = time.time()
    img = cv2.imread(path)
    # print(img.shape)
    # cv2.imshow('Mask_dilate', img)
    # cv2.waitKey()
    img = picture_process(img)
    Data=''
    pictures = Cutting_picture(img)
    h1=Par.Data_H2
    for i in range(h1):
        Dz, Vz = Decode_one(pictures[i],Par.Data_L2)
        Data += Dz
        Var += Vz
    for picture in pictures[h1:]:
        Dz , Vz = Decode_one(picture,Par.Data_L)
        Data+=Dz
        Var+=Vz
    return Data, Var

if __name__=='__main__':
    Data ,var= Decode('nn.jpg')
    print(len(Data))

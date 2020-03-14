import cv2
import numpy as np

lower_red = np.array([160, 60, 60])
upper_red = np.array([180, 255, 255])

lower_red2 = np.array([0, 60, 60])
upper_red2 = np.array([10, 255, 255])

lower_yellow = np.array([10, 100, 100])
upper_yellow = np.array([45, 255, 255])


lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

lower_green = np.array([35, 43, 46])
upper_green = np.array([77, 255, 255])



#颜色过滤
def filter(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # cv2.namedWindow('Mask_dilate', 0)
    # cv2.imshow('Mask_dilate', mask)
    # cv2.waitKey()
    return mask

def ficontrol(image,color):
    if(color=='red'):
        image1 = filter(image,lower_red, upper_red)
        image2 = filter(image,lower_red2, upper_red2)
        image = image1+image2
    elif(color=='blue'):
        image = filter(image, lower_blue, upper_blue)
    elif(color=='yellow'):
        image = filter(image, lower_yellow, upper_yellow)
    else:
        image = filter(image, lower_green, upper_green)
    return image

def fi_map(total):
    return ficontrol(total[0], total[1])

def Color(image):
    colors = ['red', 'blue', 'yellow', 'green']
    image = [image]*4
    totals = list(zip(image, colors))
    images = list(map(fi_map, totals))
    counts = list(map(np.sum, images))
    a = max(counts)
    # if(a<=10):return 'ignore'
    return colors[counts.index(a)]

if __name__ == '__main__':
    image =cv2.imread('0185.png')
    a= Color(image)
    print(a)
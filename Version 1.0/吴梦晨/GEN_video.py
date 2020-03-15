# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:12:40 2020

@author: 吴梦晨
"""
import os
import cv2
# fps = 10  # 帧率
 
def Gen_Video(imagesPath ,name_path, fps=10):
      # 包含图片的文件夹
    # imagesPath = os.path.abspath(imagesPath)
    # print(imagesPath)

    imagesList = os.listdir(imagesPath)
    imagesList.sort()

    if imagesList == []:
        print("The entered address has no content!")

    print(imagesPath+'/'+imagesList[0])
    size = cv2.imread(imagesPath + '\\' + imagesList[0]).shape[:2]


    # size = cv2.imread('E:\上学\大二下\计算机网络\代码\MY\Picture\ 1.png').shape[:2]
    size = (size[1], size[0])

    print(size)

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

    video = cv2.VideoWriter(name_path, fourcc, fps, size)  # 调节视频大小帧率名字啥的

    frame = 0

    for imageName in imagesList:
        frame = frame + 1

        # path = os.path.abspath(os.path.join(imagesPath, imageName))
        path = imagesPath+'/'+imageName
        img = cv2.imread(path)

        video.write(img)

        print("The %d frame has been added" % frame)

    video.release()
    return 0

if __name__ == '__main__':
    Gen_Video()
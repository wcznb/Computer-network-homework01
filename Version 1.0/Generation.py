from PIL import Image
from PIL import ImageDraw
import numpy as np
# path="yy.png" #文件存储的路径
# image=Image.new("RGB",(800,600),"black")#创建一个蓝色的，大小为200*200像素的RGB图片
# drawObject=ImageDraw.Draw(image)
# drawObject.ellipse((50,50,80,80),fill="red")#在image上画一个红色的圆
# drawObject.rectangle((0,0,70,70),fill="white")
# drawObject.rectangle((10,10,60,60),fill="black")
# drawObject.rectangle((20,20,50,50),fill="white")
# image.save(path)#保存图片

class MyCode():
    def __init__(self):
        self.CODE = {'0': ['red', 'green'], '1': ['red', 'blue'], '2': ['red', 'yellow'], '3': ['green', 'red'],
                     '4': ['green', 'blue'], '5': ['green', 'yellow'], '6':['blue', 'red'], '7': ['blue','green'],
                     '8': ['blue' , 'yellow'], '9' : ['yellow', 'red']
                     }
        self.image = 0
    def Draw_point(self, x, y , drawObject):
        drawObject.rectangle((x, y, x + 90, y + 90), fill="white")
        drawObject.rectangle((x+10, y+10, x+80, y+80), fill="black")
        drawObject.rectangle((x+20, y+20, x+70, y+70), fill="white")
        drawObject.rectangle((x+30, y+30, x+60, y+60), fill="black")

    def Draw_color(self,x, y, color, drawObject):#画一个颜色点
        drawObject.rectangle((x, y, x+30,y+30), fill=color)

    def Draw_line(self,x, y, colors, drawObject):#画一行颜色点
        for i in range(len(colors)):
            self.Draw_color(x+i*30,y, colors[i], drawObject)

    def Draw(self,Data_temp, drawObject):#画全图颜色点
        H = len(Data_temp)
        if(H>21): H=21
        for i in range(H):
            if(i==10) :continue
            colors = []
            for factor in Data_temp[i]:
                colors.append(self.CODE[factor][0])
                colors.append(self.CODE[factor][1])
            colors.insert(12,"black")
            colors.insert(12, "black")
            k = i*30+90
            self.Draw_line(10, k, colors, drawObject)

    def Resolution(self,Data):#将数据分组
        L = 12
        Lengh = len(Data)
        R = int(Lengh/L)
        F = int(Lengh%L)
        Data_temp=[]
        if(R>21): R = 21
        for i in range(R):
            k = i*L
            Z = Data[k:k+L]
            Data_temp.append(Z)
        if(F!=0):Data_temp.append(Data[-F:])
        return Data_temp

    def QRC(self,Data):
        #初始化画笔和画板
        image = Image.new("RGB", (810, 810),"black")#, "black"
        drawObject = ImageDraw.Draw(image)
        #画定位点
        self.Draw_point(0,0,drawObject)
        self.Draw_point(0,720,drawObject)
        self.Draw_point(720, 0, drawObject)
        # self.Draw_point(720, 720, drawObject)
        #画图
        # a = self.Resolution(Data)
        # print(a)
        self.Draw(self.Resolution(Data),drawObject)
        self.image = image
        # image.save("yy.png")#保存图片
        return image

    def save(self,path, count=0):
        colors=['red', 'blue', 'green', 'yellow']
        drawObject = ImageDraw.Draw(self.image)
        drawObject.rectangle((90, 0, 720, 90), fill=colors[count%4])
        self.image.save(path)


if __name__=="__main__":
    a = MyCode()#
    Data = "9141498411409852140895624564987897974564132131546465465465415621498615485297679879431458679815548913213256546987984984510654189747494812315646579810751202310841897110783604789102498571204987120489710924578304358946543120654808944189864870869178434070387407834115228972034578028349754802935"

    print(len(Data))
    a.QRC(Data)
    a.save("yy.png")
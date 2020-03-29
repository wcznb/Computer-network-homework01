from PIL import Image
from PIL import ImageDraw
from SENDCODE.Parameter import par

Par = par()
Lengh = Par.Lengh
Width = Par.Width
Point_size = Par.Point_size#点的宽度
D_size = Par.D_size#定位点像素宽度
Data_L = int(Par.Data_L/2)
Data_H = Par.Data_H
Data_L2 = int(Par.Data_L2/2)
Data_H2 = Par.Data_H2
Total_Data = int(Par.Total/2)
T2 = int(Par.T2/2)
T1 = int(Par.T1/2)

class MyCode():
    def __init__(self):
        self.CODE = Par.CODE
        self.image = 0
    def Draw_point(self, x, y , drawObject):
        drawObject.rectangle((x, y, x + 9*D_size, y + 9*D_size), fill="white")
        drawObject.rectangle((x+D_size, y+D_size, x+8*D_size, y+8*D_size), fill="black")
        drawObject.rectangle((x+2*D_size, y+2*D_size, x+7*D_size, y+7*D_size), fill="white")
        drawObject.rectangle((x+3*D_size, y+3*D_size, x+6*D_size, y+6*D_size), fill="black")

    def Draw_color(self,x, y, color, drawObject):#画一个颜色点
        drawObject.rectangle((x, y, x+Point_size,y+Point_size), fill=color)

    def Draw_line(self,x, y, colors, drawObject):#画一行颜色点
        for i in range(len(colors)):
            self.Draw_color(x+i*Point_size,y, colors[i], drawObject)

    def Resolution(self,Data):
        Data_temp=[]
        step=4
        index=0
        for h in range(Data_H2):
            z=[]
            for l in range(Data_L2):
                z.append(Data[index:index+step])
                index+=step
            Data_temp.append(z)
        for h in range(Data_H):
            z=[]
            for l in range(Data_L):
                z.append(Data[index:index+step])
                index+=step
            Data_temp.append(z)
        return Data_temp

    def Draw(self, Data_temp, drawObject):
        H = len(Data_temp)
        for i in range(H):
            colors = []
            for k in Data_temp[i]:
                colors.append(self.CODE[k][0])
                colors.append(self.CODE[k][1])
            if(i<6):
                x=9*D_size
            else:
                x=D_size
            y=i*Point_size
            self.Draw_line(x, y, colors, drawObject)


    def QRC(self,Data):
        #初始化画笔和画板
        image = Image.new("RGB", (Lengh, Width),"black")#, "black"
        drawObject = ImageDraw.Draw(image)
        #画定位点
        self.Draw_point(0,0,drawObject)
        self.Draw_point(0,Width-9*D_size,drawObject)
        self.Draw_point(Lengh-9*D_size, 0, drawObject)
        #画图
        self.Draw(self.Resolution(Data), drawObject)
        self.image = image

        # image.save("yy.png")#保存图片
        return image
    def save(self, path, count=0):
        colors=['red', 'blue', 'green', 'yellow']
        drawObject = ImageDraw.Draw(self.image)
        drawObject.rectangle((9*D_size, Width-9*D_size, Lengh, Width), fill=colors[count%4])
        self.image.save(path)

if __name__=='__main__':
    a = MyCode()
    Data=''
    for i in range(480):
        Data+='1000'
    a.QRC(Data)
    a.save('yy.png')
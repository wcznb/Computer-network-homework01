from SENDCODE.Generation import MyCode
from SENDCODE.Parameter import par


Par = par()
Lengh = Par.Lengh
Width = Par.Width
Point_size = Par.Point_size#点的宽度
D_size = Par.D_size#定位点像素宽度
Data_L = Par.Data_L
Dara_H = Par.Data_H
One_T = int(Par.Total*2)

def Trans(Data):
    Data_temp=''
    zero='00000000'
    for c in Data:
        z = str(bin(c))[2:]
        z = zero[0:8-len(z)]+z
        Data_temp+=z
    return Data_temp

def Code(Data, count, path):
    Data = Trans(Data)
    L = int(len(Data)/One_T)
    Data = Data[0:L*One_T]
    encode = MyCode()
    for i in range(L):
        index = i*One_T
        encode.QRC(Data[index: index+One_T])
        count += 1
        name = '0000' + str(count)
        name = name[len(name) - 4:]
        print(name)
        encode.save(path+'/'+str(name)+'.png', count)
    return count

if __name__ == '__main__':
    Data = "asdfoihafdgskdjlfghdldflgh;dflgjhewruiotr9ty8r76yt9u7r6yt89ur6ty89u7skjfgasdfdsfasdIHUOIUOHHUIOHUIOsdfg45s6d5fgr8t97y98ret7yhlskdfghlsdkghsdjlkfhgweryouitrewt897dgf4h65ghfd4867tyr869truytyr8DASFGSFDGGSDF4G98S7TY984GF89H74FD98GH4FDG4H89GFH4DH48F94H98DFG4D89FGT7Y9RTD8Y7ER98TY79ER"
    Code(Data, 0 ,'E:/Generation/Last/Picture')

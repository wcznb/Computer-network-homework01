from RECIVE.Cap import capture
from RECIVE.Translation import Translation
import os
import time
import struct

def write0xFF(path):
    binfile = open('./BIN_TEST/'+path, 'rb')  # 打开二进制文件
    size = os.path.getsize('./BIN_TEST/'+path)
    file = open('./var/' + path[0:2] + 'var.bin', 'wb')
    binfilein = open('./BIN/' + path, 'rb')

    for i in range(size):
        data1 = binfile.read(1)
        num1 = struct.unpack('B', data1)
        data2 = binfilein.read(1)
        num2 = struct.unpack('B', data2)
        # print(num1, num2)
        if (num1 == num2):
            a = int('11111111', 2)
            content = a.to_bytes(1, 'big')
        else:
            s1 = str(bin(num1[0]))
            s2 = str(bin(num2[0]))
            # print(str(bin(num1[0])))
            zero = '00000000'
            s1 = zero[len(s1)-2:]+s1[2:]
            s2 = zero[len(s2)-2:]+s2[2:]
            # print(s1, s2)
            # print(s1, s2)
            z = ''
            for i in range(8):
                if(s1[i]==s2[i]):
                    z+='1'
                else:
                    z+='0'
            a = int(z, 2)
            content = a.to_bytes(1, 'big')
        # print(content)
        file.write(content)
    file.close
    binfile.close()
    binfilein.close()

def Receive_main(Video_name, out_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # capture('out3.mp4', 'E:\Generation\MY3')
    capture(Video_name, current_dir)
    path = current_dir+"\Picture_cap"
    # ticks = time.time()
    Trans,T, Var= Translation(path)
    # ticks2 = time.time()
    # ticks = ticks2-ticks
    with open("./BIN_TEST/"+out_name+'.bin', "wb") as file:
        for data in Trans:
            content = data.to_bytes(1, 'big')
            file.write(content)
    file.close()
        # file.write(Trans.encode('ascii'))
    # with open("./var/"+out_name+'.bin', "wb") as file:
    #     for data in Var:
    #         content = data.to_bytes(1, 'big')
    #         file.write(content)
    write0xFF(out_name+'.bin')
    return Trans,T

if __name__=="__main__":
    D,T=Receive_main('e5.mp4', 'e5')

    print(((len(D))*8)/T)
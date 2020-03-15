from SENDER_CODE.Generation import MyCode

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

def Trans(Data):
    Data_temp=''
    for i in Data:
        if(i in wordvect.keys()):
            Data_temp+=wordvect[i]
    return Data_temp

def Code(Data, count, path):
    Data = Trans(Data)
    char_num = 252
    L = int(len(Data)/char_num)
    O = int(len(Data)%char_num)
    encode = MyCode()
    for i in range(L):
        index = i*char_num
        encode.QRC(Data[index: index+char_num])

        count += 1
        name = '0000' + str(count)
        name = name[len(name) - 4:]
        print(name)
        encode.save(path+'/'+str(name)+'.png', count)
    if(O):
        encode.QRC(Data[-O:])
        count += 1
        name = '0000' + str(count)
        name = name[len(name) - 4:]
        print(name)
        encode.save(path+'/'+str(name)+'.png', count)
    return count

if __name__ == '__main__':
    Data = "asdfoihafdgskdjlfghdldflgh;dflgjhewruiotr9ty8r76yt9u7r6yt89ur6ty89u7skjfgasdfdsfasdIHUOIUOHHUIOHUIOsdfg45s6d5fgr8t97y98ret7yhlskdfghlsdkghsdjlkfhgweryouitrewt897dgf4h65ghfd4867tyr869truytyr8DASFGSFDGGSDF4G98S7TY984GF89H74FD98GH4FDG4H89GFH4DH48F94H98DFG4D89FGT7Y9RTD8Y7ER98TY79ER"
    Code(Data, 0 ,'./Picture')

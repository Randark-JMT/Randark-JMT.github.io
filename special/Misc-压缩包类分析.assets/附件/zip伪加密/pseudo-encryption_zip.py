import struct
out_HEX = []
head = [b'P', b'K']


def main():
    print("$ zip伪加密自动解密脚本 $",end="\n\n")
    infile = open("D:\\Downloads\\test.zip", "rb")
    i: int = 0
    while i <= 1:
        c = infile.read(1)
        # print(c)
        if c == head[i]:
            out_HEX.append(ord(c))
        else:
            exit()
        i += 1
    while 1:
        c = infile.read(1)
        if not c:
            break
        out_HEX.append(ord(c))
    infile.close()
    # print(out_HEX)

    len_out = len(out_HEX)
    i: int = 0
    while i < len_out:
        if out_HEX[i] == 80 and out_HEX[i+1] == 75 and out_HEX[i+2] == 3 and out_HEX[i+3] == 4: # zip文件源数据区
            print("zip文件源数据区： ",end="")
            for letter in out_HEX[i:i+4]:
                print(letter,end=" ")
            print("-->",end=" ")
            for letter in out_HEX[i:i+4]:
                print(hex(letter),end=" ")
            print("")
            print("zip文件源数据区加密状态： ",end="")
            print(str(out_HEX[i+6])+" "+str(out_HEX[i+7]))
            print("\n")
            out_HEX.pop(i+6)
            out_HEX.insert(i+6,0)
            out_HEX.pop(i+7)
            out_HEX.insert(i+7,0)
        elif out_HEX[i] == 80 and out_HEX[i+1] == 75 and out_HEX[i+2] == 1 and out_HEX[i+3] == 2: # zip文件源数据目录区
            print("zip文件源数据目录区 ",end="")
            for letter in out_HEX[i:i+4]:
                print(letter,end=" ")
            print("-->",end=" ")
            for letter in out_HEX[i:i+4]:
                print(hex(letter),end=" ")
            print("")
            print("zip文件源数据目录区加密状态： ",end="")
            print(str(out_HEX[i+6])+" "+str(out_HEX[i+7]))
            print("\n")
            out_HEX.pop(i+8)
            out_HEX.insert(i+8,0)
            out_HEX.pop(i+9)
            out_HEX.insert(i+9,0)
        i += 1

    with open("D:\\Downloads\\out.zip", "wb") as outfile:
        for bytes_ in out_HEX:
            # print(bytes_)
            # print(struct.pack("B", bytes_))
            outfile.write(struct.pack("B", bytes_))
        print("文件已解密")


if __name__ == '__main__':
    main()

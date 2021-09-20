import zipfile
import string
import binascii


def CrackCrc(crc):
    for i in dic:
        for j in dic:
            for k in dic:
                for h in dic:
                    s = i + j + k + h
                    if crc == (binascii.crc32(s.encode())):
                        f.write(s)
                        return


def CrackZip():
    for i in range(0, 68):
        file = "D:\\Downloads\\b2ca8799-13d7-45df-a707-94373bf2800c\\"+'out' + str(i) + '.zip'
        crc = zipfile.ZipFile(file, 'r').getinfo('data.txt').CRC
        CrackCrc(crc)
        print('\r' + "loading：{:%}".format(float((i + 1) / 68)), end='')


dic = string.ascii_letters + string.digits + '+/='
f = open('D:\\Downloads\\b2ca8799-13d7-45df-a707-94373bf2800c\\out.txt', 'w')
print("CRC32 begin")
CrackZip()
print("CRC32 finished")
f.close()


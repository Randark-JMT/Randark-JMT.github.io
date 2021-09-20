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

dic = string.ascii_letters + string.digits + '+/='
with open('D:\\Downloads\\b2ca8799-13d7-45df-a707-94373bf2800c\\out.txt', 'w') as f:
    print("CRC32begin")
    file = "D:\\Downloads\\b2ca8799-13d7-45df-a707-94373bf2800c\\"+'out1.zip'
    crc = zipfile.ZipFile(file, 'r').getinfo('data.txt').CRC
    CrackCrc(crc)
    print("CRC32finished")
import binascii

dic = "0123456789"

for x1 in dic:
    for x2 in dic:
        for x3 in dic:
            for x4 in dic:
                for x5 in dic:
                    s = x1+x2+x3+x4+x5
                    crc = binascii.crc32(s)&0xFFFFFFFF
                    if (crc==0xec169070):
                        print hex(crc),s

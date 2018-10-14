#!/usr/bin/env python

import binascii

dic = r"0123456789"

dic1 = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "

for x1 in dic:
    for x2 in dic:
        for x3 in dic:
            for x4 in dic:
                for x5 in dic:
                    s = x1+x2+x3+x4+x5
                    crc = binascii.crc32(s)&0xFFFFFFFF
                    if (crc==0x176753F1 or crc==0xded0067e):
                        print hex(crc),s
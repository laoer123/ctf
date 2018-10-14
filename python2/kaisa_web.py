# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:12:06 2018

@author: laoer123
"""

import re

s0 = '''
BE5650G - 0BA CH50A A0D THE CH50ESE 9505ST4O 1F EDUCAT510 A001U0CED 910DAO A0 ENTE0S510 1F THE54 EN5ST50G 2A4T0E4SH52 T1 50C14214ATE F5T0ESS A0D BAS7ETBA88 DEVE8129E0T 50 E8E9E0TA4O, 95DD8E A0D H5GH SCH118S AC41SS CH50A.THE A001U0CE9E0T MAS 9ADE AT A S5G050G CE4E910O T1DAO BO 0BA CH50A CE1 DAV5D SH1E9A7E4 A0D NU TA1, D54ECT14 GE0E4A8 1F THE 50TE40AT510A8 C112E4AT510 A0D ENCHA0GE DE2A4T9E0T 1F THE 9505ST4O 1F EDUCAT510.
"ME A4E ENC5TED T1 B41ADE0 1U4 2A4T0E4SH52 M5TH THE 9505ST4O 1F EDUCAT510 T1 9A7E A 810G-8AST50G 592ACT 10 THE 85VES 1F CH50ESE STUDE0TS TH41UGH A 6150T8O-DES5G0ED BAS7ETBA88 CU445CU8U9 A0D A M5DE 4A0GE 1F SCH118 BAS7ETBA88 241G4A9S," SA5D SH1E9A7E4. "TH5S C1995T9E0T 9A47S A01THE4 958EST10E 50 THE 0BA'S O1UTH A0D BAS7ETBA88 DEVE8129E0T EFF14TS 50 CH50A." F8AG { GS182D9HCT9ABC5D}
'''
#flag{1ae3ed9f-ec9a-48d2-aad8-36b03706e7a7}

char = 'abcdefghijklmnopqrstuvwxyz'
s2 = []

#s1 = re.findall('[a-z]',s0)
#s1 = ''.join(s1)
#print len(s1)
#result = []

for i in s0:
    if i.isdigit():
        index = int(i) + 13
        if index > 25:
            index -= 26
        s2.append(char[index])
    else:
        s2.append(i)
print ''.join(s2).lower()

#
#for i in s1:
#    s1_index = char.index(i)
##    print s1_index
#    if s1_index % 2 == 0:
#        s1_index += 6
#        if s1_index > 25:
#            s1_index -= 26
#        result.append(char[s1_index])
#    else:
#        s1_index -= 6
#        if s1_index < 0:
#            s1_index += 26
#        result.append(char[s1_index])
#
#print len(result)
##print ''.join(result)
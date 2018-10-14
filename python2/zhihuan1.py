# encoding:utf-8

import numpy as np
import math
from functools import reduce

def DecryptT(ciphertext, key):
    ciphertext = list(ciphertext)
    for i in range(key - len(ciphertext) % key):
        k = int(math.ceil(len(ciphertext) / key) * (key - i) - 1)
        ciphertext.insert(k, '')
    c = np.array(ciphertext)
    c.shape = key, -1
    return reduce(lambda x, y: x + y, [''.join(c[:, i]) for i in range(int(math.ceil(len(ciphertext) / key)))])

if __name__ == "__main__":
    for j in range(1,100):
        print(DecryptT('10dRRBr~3ux<Wxz14E>Fatau~Exituz%f,oz|hxT}hg{oAhflaI1QP', j))

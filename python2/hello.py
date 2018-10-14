# -*- coding: utf-8 -*-
from base64 import *
s = "hello world!"
b64 = b64encode(s)
print b64
print b64decode(b64)
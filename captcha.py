"""
This is a program to print CAPTCHA
"""

import random
import string as s

s1 = s.ascii_letters + s.digits
print(s1)
print(len(s1))

captcha = ""
for i in range(0, 5):
    # print(random.randrange(0, 62))
    index = random.randrange(0, 62)
    captcha += s1[index]

print(captcha)
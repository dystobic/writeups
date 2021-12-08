#!/usr/bin/python3

build = r"""9xLmMiI2znmPam'D_A_1:RQ;Il\*7:%i".R<"""

r2_table = {}
for i in range(33, 127):
    for j in range(33, 127):
        b = ''
        b += chr((2 * i - j + 153) % 93 + 33)
        b += chr((j - i + 93) % 93 + 33)
        r2_table[b] = chr(i) + chr(j)

r2 = ''
for i in range(0, len(build) - 1, 2):
    r2 += r2_table[build[i] + build[i+1]]

flag = ''
for c in r2:
    flag += chr(158 - ord(c))

print(flag)


#!/usr/bin/python3

a = []
a.append(1739411)
a.append(1762811)
a.append(1794011)
a.append(1039911)
a.append(1061211)
a.append(1718321)
a.append(1773911)
a.append(1006611)
a.append(1516111)
a.append(1739411)
a.append(1582801)
a.append(1506121)
a.append(1783901)
a.append(1783901)
a.append(1773911)
a.append(1582801)
a.append(1006611)
a.append(1561711)
a.append(1039911)
a.append(1582801)
a.append(1773911)
a.append(1561711)
a.append(1582801)
a.append(1773911)
a.append(1006611)
a.append(1516111)
a.append(1516111)
a.append(1739411)
a.append(1728311)
a.append(1539421)

b = ''

for i in a:
    c = str(i)[::-1]
    c = c[:-1]
    c = int(c)
    c = c ^ 5
    c = c - 55555
    c = c // 555
    b = b + chr(c)

print(b)

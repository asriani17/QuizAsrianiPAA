import numpy as  python
##Asriani
##F55121087

sumofmultipe = []
y = 3
while y < 20:
    if y % 3 == 0:
        sumofmultipe.append(y)
    elif y & 5 == 0:
        sumofmultipe.append(y)
    y = y + 3
print (sumofmultipe)
sums = 0
for i in sumofmultipe:
    sums = sums + i
print (sums)

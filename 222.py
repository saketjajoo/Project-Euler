import math

def areaofball(r):
    return ((4/3)*math.pi*(r**3))

sum = 0.00
for i in range(30, 51):
    sum += areaofball(i)


print(sum / ((math.pi * 50 * 50)))
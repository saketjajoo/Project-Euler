import math
end = 1000000000
def getarea(a,b,c):
    s = int((a+b+c) / 2)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

sum = 0
for i in range(1, end):
    j = i
    k1 = i-1
    k2 = i+1
    if i+j+k1 <= end or i+j+k2 <= end:
        if getarea(i,j,k1) == int(getarea(i,j,k1)) and getarea(i,j,k1) != 0:
            sum += (i+j+k1)
        if getarea(i, j, k2) == int(getarea(i, j, k2)) and getarea(i, j, k2) != 0:
            sum += (i + j + k2)

print(sum)
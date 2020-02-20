def getfn(n):
    n = str(n)
    temp = 0
    for i in range(len(n)):
        temp += ((int(n[i]))**2)
    return temp

sum = 0
for i in range(1, 10000000001):
    sum += getfn(i*i)
    print(i)

print(sum)

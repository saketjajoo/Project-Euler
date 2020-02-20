def getsumofdig(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

arr = []

i = 1
j = 10
while i <= 30:
    pow = 1
    sod = getsumofdig(j)
    if sod != 1:
        while sod**pow < j:
            pow += 1
        if sod**pow == j:
            arr.append(j)
    j += 1

print(arr[-1])

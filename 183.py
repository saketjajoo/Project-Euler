def isterminating(n, d):
    while d%2 == 0:
        d = d/2
    while d%5 == 0:
        d = d/5

    return d == 1

def getpmax(n):
    max = 1.00
    nr = n
    dr = max
    for i in range(int(n/2), 0, -1):
        if (n/i)**i >= max:
            max = (n/i)**i
            dr = i
    return nr,dr

sum = 0
for i in range(5, 10000):
    x, y = getpmax(i)
    if isterminating(x**y, y**y):
        sum -= i
    else:
        sum += i

print(sum)



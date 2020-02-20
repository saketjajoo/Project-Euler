def rotate(n):
    no = str(n)
    temp = no[-1]
    temp += no[0:len(no)-1]
    return int(temp)

sum = 0
for i in range(10, 10**100):
    n = rotate(i)
    if i>n:
        if (i / n) == int(i/n):
            sum += int(str(i)[len(str(i)) - 5 :])
            #print(i)
    else:
        if (n / i) == int(n / i):
            sum += int(str(n)[len(str(n)) - 5:])
            #print(n)
print(sum)
def init():
    d = {}
    for i in range(0,10):
        d[i] = 0
    return d

count = 0
start = 100000000000000000
end = 999999999999999999
for i in range(start, end):
    d = init()
    flag = 0
    no = str(i)
    for l in range(len(no)):
        if d[int(no[l])] > 3:
            flag = 1
            break
        else:
            d[int(no[l])] += 1
    if flag == 0:
        count +=1

print(count)


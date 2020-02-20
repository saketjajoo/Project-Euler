
maxlen = 0

start = 13
ans = 0
while start <= 1000000:
    chain = []
    temp = start
    while 1 not in chain:
        if temp % 2 == 0:
            temp  = int(temp/2)
            chain.append(temp)
        else:
            temp = 3*temp + 1
            chain.append(temp)
    if len(chain)>=maxlen:
        maxlen = len(chain)
        ans = start
    start+=1

print(maxlen)
print(ans)
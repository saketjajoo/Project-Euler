def divsum(n):
    ans = 0
    for i in range(1,int(n/2)):
        if n%i == 0:
            ans += i
    return ans


s = []
for i in range(1,10000):
    for j in range(1,10000):
        if i!=j:
            if divsum(i) == divsum(j):
                s.append(i)
                s.append(j)

print(sum(set(s)))



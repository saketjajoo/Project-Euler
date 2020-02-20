import math

def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True

def getalltruncs(n):
    no = str(n)
    l = []
    for i in range(1,len(no)):
        l.append(int(no[i:]))
    no = str(n)
    for i in range(len(no)-2,-1,-1):
        l.append(int(no[0:i+1]))
    return l


start = 11
ans = 0

for ele in range(start, 1000000):
    flag = 0
    if isprime(ele):
        x = getalltruncs(ele)
        for i in x:
            if isprime(i):
                flag = 0
            else:
                flag = 1
                break
        if flag == 0:
            ans += ele
        else:
            continue
    start+=1

print(ans)


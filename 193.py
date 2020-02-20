import math

def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def getprimes(n):
    l = []
    for i in range(2, n+1):
        if isprime(i):
            l.append(i)
    return l


count = 8
end = 2**50
l = getprimes(end)
for i in range(12, end):
    flag = 0
    for j in range(len(l)):
        if i % (l[j]**2) == 0:
            flag = 1
            break
    if flag == 0:
        count += 1
print(count)

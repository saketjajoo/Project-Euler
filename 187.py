import math

def isprime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def getnoofdivisors(n):
    count = 0
    for i in range(2, int(n/2)+1):
        if count > 2:
            return -1
        if isprime(i) and n%i == 0:
            count += 1
    return count

ans = 0
for i in range(2, 10000):
    if not isprime(i*i):
        ans += 1

print(ans)

for i in range(2, 10**8):
    if getnoofdivisors(i) == 2:
        ans += 1

print(ans)
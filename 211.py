import math

def getsumofsqofdivisors(n):
    ans = 0
    for i in range(1, n+1):
        if n%i == 0:
            ans += (i*i)
    return ans

def isperfectsq(n):
    if (math.isqrt(n) ** 2) == n:
        return True
    else:
        return False

ans = 0
end = 64000000
for i in range(1, end):
    if isperfectsq(getsumofsqofdivisors(i)):
        ans += i
print(ans)
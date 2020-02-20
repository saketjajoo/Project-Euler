m = 1000000
ans = 6


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


for i in range(10000, 1000001):
    if sorted(str(i)) == sorted(str(phi(i))):
        if (i / phi(i)) <= m:
            m = (i / phi(i))
            ans = i
print(ans)

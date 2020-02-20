def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

ans = 0
for n in range(1, 101):
    for r in range(0, n+1):
        if int((fact(n) / (fact(r) * fact(n-r)))) >= 1000000:
            ans += 1

print(ans)

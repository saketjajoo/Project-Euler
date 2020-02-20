def fact(n):
    if n == 1 or n == 0:
        return 1
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

val = 1000000000000
print(fact(val))
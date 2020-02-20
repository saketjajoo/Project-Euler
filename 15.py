def fact(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s

print(int(fact(40) / (fact(20)*fact(20))))
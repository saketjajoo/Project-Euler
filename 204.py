def generatedivisors(n):
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    return divisors

ans = 0
for i in range(1, 10**9):
    d = generatedivisors(i)
    flag = 0
    for j in range(len(d)-1,-1,-1):
        if d[j] > 97:
            flag = 1
            break
    if flag == 0:
        ans += 1
print(ans)
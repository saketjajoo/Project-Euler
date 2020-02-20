def getnoofdivisors(n):
    count = 2
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            count += 1
    return count

ans = 0
for i in range(2, 10**7):
    if getnoofdivisors(i) == getnoofdivisors(i+1):
        ans += 1
    print(i)
print(ans)
def fact(n):
    f = 1
    for i in range(1,n+1):
        f*=i
    return f

ans = str(fact(100))
sum = 0
for ele in ans:
    sum += int(ele)
print(sum)
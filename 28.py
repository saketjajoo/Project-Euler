ans = 1
ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, 1002, 2))
print(ans)
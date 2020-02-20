TOTAL = 200
ways = [1] + [0] * TOTAL
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(len(ways) - coin):
        ways[i + coin] += ways[i]
print(ways[-1])
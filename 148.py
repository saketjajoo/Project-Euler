pascaltriangle = [[1], [1, 1]]
end = 10**9
count = 3

for i in range(2, end):
    tp = [1]
    for j in range(1, i):
        tp.append((pascaltriangle[i-1][j-1] + pascaltriangle[i-1][j]))
        if (pascaltriangle[i-1][j-1] + pascaltriangle[i-1][j])%7 != 0:
            count += 1
    tp.append(1)
    count += 2
    pascaltriangle.append(tp)

print(count)
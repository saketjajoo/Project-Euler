sum = 0

for i in range(1,100):
    for j in range(1,100):
        temp = str(int(i**j))
        tempsum = 0
        for ele in temp:
            tempsum += int(ele)
        if tempsum > sum:
            sum = tempsum
print(sum)

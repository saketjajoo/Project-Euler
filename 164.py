count = 0

for i in range(10000000000000000000, 1000000000000000000000):
    no = str(i)
    for j in range(len(no)-2):
        if int(no[j]) + int(no[j+1]) + int(no[j+2]) > 9:
            continue
    count += 1

print(count)
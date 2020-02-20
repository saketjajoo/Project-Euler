f = open("words.txt", "r+")
ans = f.read().split(",")


arr = []
for i in range(len(ans)):
    ans[i] = ans[i].strip("\"")
    tp = 0
    for ele in ans[i]:
        tp += (ord(ele)-64)
    arr.append(tp)

traingles = []
count = 0
for i in range(1, 100):
    traingles.append(int(i*(i+1) / 2))

for ele in arr:
    if ele in traingles:
        count += 1

print(count)
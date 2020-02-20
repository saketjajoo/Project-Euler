f = open("base_exp.txt","r")
data = f.read().split()
max = 0
pos = 0
for i in range(len(data)):
    base = int(data[i].split(",")[0])
    exp = int(data[i].split(",")[1])
    val = base**exp
    if val >= max:
        max = val
        pos = i
print(pos)
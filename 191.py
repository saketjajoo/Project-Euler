import itertools

ans = 0
a = ["O","A","L"]
l = list(itertools.product(a, repeat=30))

for i in range(len(l)):
    l[i] = "".join(l[i])
    if ("AAA"in l[i]) or (l[i].count("L") > 1):
        continue
    else:
        ans += 1
print(ans)
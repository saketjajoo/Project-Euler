import itertools

p = [1,2,3,4]
c = [1,2,3,4,5,6]

pl = list(itertools.product(p, repeat=9))
cl = list(itertools.product(c, repeat=6))

tp = []
tc = []

for i in range(len(pl)):
    tp.append(sum(pl[i]))

for i in range(len(cl)):
    tc.append(sum(cl[i]))

ans = 0
count = 0

# 12230590464 iterations

for i in range(len(tp)):
    for j in range(len(tc)):
        count += 1
        print(count)
        if tc[j] < tp[i]:
            ans += 1
print(ans)
print(count)

print(ans / count)

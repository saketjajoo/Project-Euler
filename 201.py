import itertools

s = []
for i in range(1, 101):
    s.append(i**2)

l = list(itertools.combinations(s, 50))

sum_list = []
for i in range(len(l)):
    sum_list.append(sum(l[i]))
ans = sum(set(sum_list))
print(ans)
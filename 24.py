import itertools

arr = list(range(10))
temp = itertools.islice(itertools.permutations(arr), 999999, None)
print("".join(str(x) for x in next(temp)))

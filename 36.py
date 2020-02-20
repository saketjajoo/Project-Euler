s = 0
for i in range(1, 1000000):
    n1 = str(i)
    n2 = str(bin(i))
    n2 = n2[2:]
    if n1[::] == n1[::-1] and n2[::] == n2[::-1]:
        s += i
print(s)
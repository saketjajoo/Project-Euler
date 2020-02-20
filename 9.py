PERIMETER = 1000
flag = 0
for a in range(1, PERIMETER + 1):
    if flag == 1:
        break
    for b in range(a + 1, PERIMETER + 1):
        c = PERIMETER - a - b
        if a * a + b * b == c * c:
            print(a*b*c)
            flag = 1
            break
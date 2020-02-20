import math

def isperfectsq(n):
    if n == 0:
        return False
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False

end = 10000000
flag = 0
for x in range(1, end):
    if flag == 1:
        break
    for y in range(1, end):
        if flag == 1:
            break
        for z in range(1, end):
            if isperfectsq(x+y) and isperfectsq(abs(x-y)) and isperfectsq(x+z) and isperfectsq(abs(x-z)) and isperfectsq(y+z) and isperfectsq(abs(y-z)):
                print(x)
                print(y)
                print(z)
                print(x+y+z)
                flag = 1
                break


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

def isInside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False

f = open("triangles.txt","r")
data = f.read().split()

tr_coord = []
for i in range(len(data)):
    l = data[i].split(",")
    for i in range(6):
        l[i] = int(l[i])
    tr_coord.append(l)

count = 0
for i in range(len(tr_coord)):
    if isInside(tr_coord[i][0], tr_coord[i][1], tr_coord[i][2], tr_coord[i][3], tr_coord[i][4], tr_coord[i][5], 0, 0):
        count += 1

print(count)



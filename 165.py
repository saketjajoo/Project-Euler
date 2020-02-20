def isPointOnLine(l, x, y):
    x1 = l[0]
    y1 = l[1]
    x2 = l[2]
    y2 = l[3]
    if y == ((((y2-y1) / (x2-x1)) * (x - x1)) + y1):
        return True
    else:
        return False


def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

sn = [290797]
tn = []
count = 0
for i in range(1, 20002):
    sn.append(((sn[i-1] * sn[i-1]) % 50515093))
    tn.append((sn[i-1] % 500))

tn = tn[1:]

lines = []
for i in range(0,len(tn),4):
    lines.append([tn[i], tn[i+1], tn[i+2], tn[i+3]])

for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        A = [lines[i][0], lines[i][1]]
        B = [lines[i][2], lines[i][3]]
        C = [lines[j][0], lines[j][1]]
        D = [lines[j][2], lines[j][3]]
        if (intersect(A,B,C,D)) and (not(isPointOnLine(lines[i], C[0], C[1]))) and (not(isPointOnLine(lines[i], D[0], D[1]))):
            count += 1

print(count)

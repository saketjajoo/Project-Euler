import math

def isprime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def getcircle(n):
    no = str(n)
    l = []
    for i in range(len(no)):
        number = no[i:] + no[:i]
        l.append(number)
    return l

count = 2
for i in range(11, 1000000):
    flag = 0
    if isprime(i):
        x = getcircle(i)
        for ele in x:
            if isprime(int(ele)):
                flag = 0
                continue
            else:
                flag = 1
                break
        if flag == 1:
            continue
        else:
            count += 1

print(count)
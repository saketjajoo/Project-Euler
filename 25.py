import itertools

DIGITS = 1000
prev = 1
cur = 0
for i in itertools.count():
    if len(str(cur)) > DIGITS:
        break
    elif len(str(cur)) == DIGITS:
        print(str(i))
    prev, cur = cur, prev + cur
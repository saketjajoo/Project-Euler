from urllib3.connectionpool import xrange
def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in xrange(9))
n = 138902663
while match(n*n):
    n -= 2
print(n*10)
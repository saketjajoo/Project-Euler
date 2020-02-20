primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
c = 11
no = 31

def isprime(n):
    for i in range(2,int(n//2)):
        if n%i == 0:
            return False
    return True

while c <= 10003:
    if isprime(no):
        primes.append(no)
        c += 1
    no+=1


print(primes[10000])
import math

end = 1000

def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False

    return True

count = 0
primes=  [2, 3, 5, 7, 11]
for i in range(12, end):
    if isprime(i):
        primes.append(i)
for i in range(2, len(primes)):
    for j in range(2, len(primes)):
        for k in range(2, len(primes)):
            if i**2 + j**3 + k**4 <= end:
                count += 1
print(count)
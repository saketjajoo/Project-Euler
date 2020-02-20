def isprime(n):
    for i in range(2,int(n//2)):
        if n%i == 0:
            return False
    return True

primes = [2,3,5,7,11]
temps = sum(primes)

c = 6
no = 13
while c <= 2000000:
    if isprime(no):
        primes.append(no)
        c+=1
        temps += no
    no+=1

print(temps)
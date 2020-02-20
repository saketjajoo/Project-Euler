n = 100

sosq = int(n*(n+1)*(2*n+1) / 6)
sqos = (int(n*(n+1)/2))**2

print(abs(sosq - sqos))
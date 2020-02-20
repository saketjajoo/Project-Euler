import math


def factorial_digit_sum(n):
	result = 0
	while n >= 10000:
		result += fdswlz[n % 10000]
		n //= 10000
	return result + fdswolz[n]



fdswolz = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
fdswlz = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]

ans = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
print(ans)
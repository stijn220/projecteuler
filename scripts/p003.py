# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from euler import solution, is_prime
import math

@solution
def solve():
	n = 600851475143
	prime_factors = []
	
	while n % 2 == 0:
		prime_factors.append(2)
		n //= 2

	for i in range(3, int(math.sqrt(n)) + 1, 2):
 	   while n % i == 0:
   	     prime_factors.append(i)
   	     n //= i

	if n > 2:
	    prime_factors.append(n)
	
	prime_factors.sort()
	return prime_factors[-1]
solve()




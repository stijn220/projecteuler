# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

from euler import solution


x_range = 1000
@solution
def solve():
	multiples = []
	for x in range(1,x_range+1):
	
		x_5 = 5 * x
		x_3= 3 * x
	
		if x_5 < x_range:
			multiples.append(x_5)
		if x_3 < x_range:
			multiples.append(x_3)			
		
	multiples = list(dict.fromkeys(multiples))
		
	return sum(multiples)
		
solve()
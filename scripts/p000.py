from euler import solution, is_odd

import math


def square_list(n):
	squares = []
	for i in range(1, n+1):
		squares.append(i**2)
	return squares

def odds(a):
	odds_list = []
	for x in a:
		if is_odd(x):
			odds_list.append(x)
	return odds_list
						
@solution
def solve():
	squares = square_list(384000)
	odds_list = odds(squares)
	return sum(odds_list)
	

solve()
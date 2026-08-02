# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?

from euler import solution

@solution
def solve():
    
    x = 2520
    while not all(x % y == 0 for y in range(11, 21)):
        for y in range(1,21):
            if x % y == 0:
                x += 2520
                break
    return x

solve()
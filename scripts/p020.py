# n! means n * (n-1) * ... * 3 * 2 * 1.
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 362800,
#  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27/
# Find the sum of the digits in the number 100!.

from euler import solution
import math

@solution
def solve():
    x = math.factorial(100)
    y = 0
    for i in str(x):
        y += int(i)
    return y
    
if __name__ == "__main__":
    solve()
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

from euler import solution

@solution
def solve():
    x = str(2**1000)
    y = 0
    for i in x:
        y += int(i)
    return y

solve()
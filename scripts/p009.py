# A Pythagorean triplet is a set of three natural numbers, a b c, for which,
# a*2 + b*2 = c*2.
# For example, 3*2 + 4*2 = 9 + 16 = 25 = 5*2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from euler import solution

@solution
def solve():
    a = 1
    b = 1
    c = 0
    d = 0
    target = 1000
    while d != target:
        b += 1
        if pythagoras(a,b) > target:
            b = 1
            a += 1

        c = pythagoras(a,b)

        d=a+b+c
    print(a, b, c)
    return int(a*b*c)

def pythagoras(a,b):
    
    return (a**2 + b**2)**0.5 
    
solve()
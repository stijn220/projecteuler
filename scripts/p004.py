# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


from euler import solution, is_palindromic

@solution
def solve():
    x = y = 999
    
    palindromic = 0
    
    while x >= 100:
        if x * x <= palindromic:
            break
        while y >= 100:
            z = x * y
            if is_palindromic(str(z)):
                if z > palindromic:
                    palindromic = z
            y -= 1
        x -= 1
        y = x
    return palindromic

solve()
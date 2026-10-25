# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from euler import solution
import itertools

@solution
def solve():
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    count = 0
    for subset in itertools.permutations(digits):
        count += 1
        
        if count == 10**6:
            return "".join(subset)
if __name__ == "__main__":
    solve()

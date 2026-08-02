from euler import solution

@solution
def solve():
    
    sum_range = [i for i in range(1, 101)]
    sum_of_squares = sum(i **2 for i in sum_range)
    squares_of_sum = sum(sum_range) ** 2
    
    return squares_of_sum - sum_of_squares

solve()
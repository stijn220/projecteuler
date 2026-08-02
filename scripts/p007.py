from euler import solution, prime_generator

@solution
def solve():
    count = 0
    while True:
        for prime in prime_generator():
            count += 1
            
            if count == 10000:
                return prime
    
solve()
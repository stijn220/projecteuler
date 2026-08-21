# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from euler import solution, prime_generator

@solution
def solve():
    primes_sum = 0
    for prime in prime_generator():
        if prime < 2000000:
            primes_sum += prime
        else:
            return primes_sum

solve()


# Deze is wel beetje langsaam. De prime_generator kan geoptimaliseerd worden.
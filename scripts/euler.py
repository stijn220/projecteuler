import time
import math
from typing import Generator, List

def solution(func):
    
    def inner(*args, **kwargs):
        start = time.time()
        answer = func(*args, **kwargs)
        end = time.time()
        runtime = round(end - start, 3)
        print(f"Finished:")
        print(f"runtime = {runtime}")
        print(f"answer:")
        print(answer)
    
    return inner

#Helpers

def is_odd(x: int) -> bool:
    """Returns True if the integer is odd, else return False"""
    if x%2==0:
        return False
    else:
        return True

def is_even(x: int) -> bool:
    """Returns True if the integer is even, else return False"""
    if x%2==0:
        return True
    else:
        return False    

def is_whole(x: float) -> bool:
    """Returns True if the number is a whole number, else return False"""
    return float(x).is_integer()
    
def is_prime(x:int) -> bool:
    """Returns True if integer is a prime number, else return False"""
    if x <=1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x%i ==0:
                return False
        return True

def prime_generator() -> Generator[int]:
    """Return a stream of prime numbers"""
    primes = [2]
    yield 2
    num = 3
    while True:
        is_prime = True
        square_root = math.sqrt(num)
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
            if prime > square_root:
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 2


def is_palindromic(x:str):
    """Returns True if string is a palindromic, else return False"""
    if x == x[::-1]:
        return True
    else:
        return False
    
def factors(x:int) -> List[int]:
    factor_set = {1}
    for y in range(1, int(math.sqrt(x) + 1)):
        if x < 0:
            return []
        z = x/y
        if is_whole(z):
            factor_set.add(int(y))
            factor_set.add(int(z))
    return list(factor_set)

def collatz(x:int) -> List[int]:
    sequece = []
    while x != 1:
        sequece.append(x)
        if is_even(x):
            x = int(x/2)
        elif is_odd(x):
            x = x * 3 + 1
    sequece.append(1)
    return sequece

def binomial_coefficient(n: int, k: int) -> int:
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n-k)
    
    return int(a // (b*c))

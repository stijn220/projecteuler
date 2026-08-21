import time
import math

def solution(func):
    
    def inner(*args, **kwargs):
        start = time.time()
        answer = func()
        end = time.time()
        runtime = round(end - start, 3)
        print(f"Finished:")
        print(f"runtime = {runtime}")
        print(f"answer:")
        print(answer)
    
    return inner

#Helpers

def is_odd(x: int):
    """Returns True if the integer is odd, else return False"""
    if x%2==0:
        return False
    else:
        return True

def is_even(x: int):
    """Returns True if the integer is even, else return False"""
    if x%2==0:
        return True
    else:
        return False    
        
def is_prime(x:int):
    """Returns True if integer is a prime number, else return False"""
    if x <=1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x%i ==0:
                return False
        return True

def prime_generator():
    """Return a stream of prime numbers"""
    count = 2
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            yield count
        
        count += 1
        


def is_palindromic(x:str):
    """Returns True if string is a palindromic, else return False"""
    if x == x[::-1]:
        return True
    else:
        return False
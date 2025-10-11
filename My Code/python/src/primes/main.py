import math
import time

def main():
    n = 10
    prime_booleans = trivial_prime_finder(n)
    print(prime_booleans)
    print(sieve_of_eratosthenes(10)) # my vers have trivial faster and eratosthenes slower
    print(list_primes(10))
    
    x = 10000000
    
    start_trivial = time.time()
    trivial_prime_finder(x)
    elapsed_trivial = time.time() - start_trivial
    print(f"trivial took {elapsed_trivial:.6f} seconds.") # amount of time to 6 decimals f string -> print in pretty ways
    
    start_sieve = time.time()
    sieve_of_eratosthenes(x)
    elapsed_sieve = time.time() - start_sieve
    print(f"sieve took {elapsed_sieve:.6f} seconds.")
    
    if elapsed_sieve > 0:
        speedup = elapsed_trivial/elapsed_sieve
        print(f"Speedup: {speedup:.2f} times faster") # increases lienarly
    """
    Pseudocode below.

    TrivialPrimeFinder(n)
        primeBooleans ← array of n+1 false boolean variables
        for every integer p from 2 to n
            if IsPrime(p) is true
                primeBooleans[p] ← true
        return primeBooleans

    IsPrime(p)
        if p < 2
            return false
        for every integer k between 2 and √p
            if k is a divisor of p
                return false
        return true

    SieveOfEratosthenes(n)
        primeBooleans ← array of n+1 true boolean variables
        primeBooleans[0] ← false
        primeBooleans[1] ← false
        for every integer p between 2 and √n
            if primeBooleans[p] = true
                primeBooleans ← CrossOffMultiples(primeBooleans, p)
        return primeBooleans

    CrossOffMultiples(primeBooleans, p)
        n ← length(primeBooleans) - 1
        for every multiple k of p (from 2p to n)
            primeBooleans[k] ← false
        return primeBooleans
    """

def trivial_prime_finder(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    Parameters:
    - n (int): an integer
    Returns:
    list[bool]: a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    if n< 0:
        raise ValueError("must be nonnegative")
    
    prime_booleans = [False] * (n+1)
    
    for p in range(2, n+1):
        prime_booleans[p] = is_prime(p)
    return prime_booleans
        
def is_prime(p: int) -> bool:
    """
    Test if p is prime.
    Parameters:
    - p (int): an integer
    Returns:
    bool: True if p is prime and False otherwise.
    """
    if p < 2: 
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True
    
def sieve_of_eratosthenes (number: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n,
    implementing the "sieve of Eratosthenes" algorithm.
    Parameters:
    - n (int): an integer
    Returns:
    list: a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    if number < 0:
        raise ValueError("number must be nonnegative")
    primality = [True]*(number+1)
    primality[0] = False
    primality[1] = False
    for i in range(2, int(math.sqrt(number)+1)):
        if primality[i] == 1:
            for j in range(2, int(number/i) + 1):
                primality[j * i] = False
                
    return primality    

def list_primes(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n should be nonnegative")
    prime_list = []
    prime_booleans = sieve_of_eratosthenes(n)
    for i in range(len(prime_booleans)):
        if prime_booleans[i]:
            prime_list.append(i)
    return prime_list
    
if __name__ == "__main__":
    main()
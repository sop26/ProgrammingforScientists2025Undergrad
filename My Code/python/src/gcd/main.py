import time

def main():
    print("GCD algorithms in Python.")
    print(trivial_gcd(2, 0))
    print(euclid_gcd(2, 0))
    
    x = 34773882888 
    y = 23490000088
    
    start_trivial = time.time()
    trivial_gcd(x, y)
    elapsed_trivial = time.time() - start_trivial
    print(f"trivial_gcd took {elapsed_trivial:.6f} seconds.") # amount of time to 6 decimals f string -> print in pretty ways
    
    start_euclid = time.time()
    euclid_gcd(x, y)
    elapsed_euclid = time.time() - start_euclid
    print(f"trivial_gcd took {elapsed_euclid:.6f} seconds.")
    
    if elapsed_euclid > 0:
        speedup = elapsed_trivial/elapsed_euclid
        print(f"Speedup: {speedup:.2f} times faster") # increases lienarly
    
def euclid_gcd(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    while (a != b):
        if (a > b):
            a = a - b
        else: 
            b = b - a
    return a 
    
    
def trivial_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two integers by applying a trivial algorithm trying every possible divisor of a and b
    """
    # I should check that a and b are not negative
    
    # slight bug when one is zero
    d = 1
    
    # try every possible divisor of a and b up to their min
    if (a == 0 or b == 0):
        return max(a, b)
    for p in range(2, min(a, b) + 1):
        if a % p == 0 and b % p == 0:
            d = p
    return d
    
if __name__ == "__main__":
    main()
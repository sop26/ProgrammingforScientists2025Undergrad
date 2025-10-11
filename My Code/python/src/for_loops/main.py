import math

def main():
    print("For loops in Python.")
    print(another_factorial(10))
    print(sum_even(7))
    
def yet_another_factorial(n: int) -> int:
    for i in range(n, 0, -1):
        product *= i
    return product

def say_hi_five():
    """
    Prints "Hi" five times.
    """
    # if bottom index is 0, you can ommit it
    for _ in range(5): # _ indicates we don't need the variable
        print("Hi")
        
def sum_even(k: int) -> int:
    """
    Returns the sum of all even positive integers up to and possibly including k.
    """ 
    # sum = 0
    # for i in range(2, k+1, 2):
    #     sum += i
    # return sum

    return math.floor(k/2) * (math.floor(k/2) + 1)
# sum of regular ints 2(n/4 (n/2+1)) sum consecutive of n/2 then multiply by 2
# 2 * n/2 * 1/2 * (n/2 + 1) = floor(n/2) * (floor(n/2) + 1) 
# 

            
def another_factorial(n: int) -> int:
    if n < 0:
        print("n is", n)
        raise ValueError("Error: negative input given to factorial.")
    product = 1
    for i in range(1, n+1,): # stop omitted
        product *= i
    return product
    
    
if __name__ == "__main__":
    main()
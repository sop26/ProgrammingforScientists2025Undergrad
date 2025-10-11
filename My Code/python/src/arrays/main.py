def main():
    print("Arrays (Tuples, List) in Python")
    
    # Python represents arrays in two ways
    primes = (2, 3, 5, 9, 11) # tuple
    # tuples great when length of array is short and fixed
    # tuples are immutable - can't change individual elements, and we can't change their size
    # can update the whole tuple
    
    primes = (2, 3, 5)
    
    print(primes)
    
    empty_list = [] # or list()
    
    n = 6
    a = [0] * n
    a[0] = -8
    i = 3
    k = 4
    a[2*i - 4] = k//2 ** 4 + 1
    a[len(a) - 1] = 43
    a[-1] = 68
    print(a)
    print("a has length", len(a))
    # python has "negative indexing" - can go backwards through a list
    # lists can have multiple types in them
    mixed_list = [1, 3.14, - 42, "Hi", True]
    print(mixed_list)
    print(factorial_array(6))
    print(min_integer_array([-1, -1, 1, 3, -2]))
    c= [0]*6
    change_first_element(c)
    print(c)
    # Lists in python are pass by reference (not value)
    
def change_first_element(a: list[int]):
    a[0] = 1
    
# Variadic function takes arbitrary number of parameters
def min_integers(*numbers: int) -> int:
    """
    Returning min of an arbitrary collection of ints
    """
    # In this case, numbers is a tuple
    if len(numbers) == 0:
        raise ValueError("Error: no numbers given to min_integers")
    
    m = numbers[0]
    for val in numbers:
        if val < m:
            m = val
    return m
    
def min_integers_better(*numbers: int) -> int:
    """
    Returning min of an arbitrary collection of ints
    """
    return min_integer_array(list(numbers)) #technically works without "list"

def min_integer_array(a: int) -> int:
    """
    Return minimum value in a list of integers
    """
    if len(a) == 0:
        raise ValueError("Error: empty list given")
   
    m = 0
    for i, val in enumerate(a): # for i, val in enumerate(a) to get index and val
        if val < m or i == 0:
            m = val
    return m
    
def factorial_array(n: int) -> list[int]:
    """
    Generates a list of factorials from 0! to n! inclusively.
    """
    # check n < 0
    fact = [0] * (n+1)
    fact[0] = 1
    for k in range(1, n+1):
        fact[k] = fact[k-1] * k
    return fact
    
if __name__ == "__main__":
    main()
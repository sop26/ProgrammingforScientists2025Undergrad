def main():
    print("Functions in Python")
    x = 3
    n = sum_two_ints("", "")
    print(n)
    print(double_and_duplicate(1))
    m = 17
    print(add_one(m)) # makes a copy through k; m doesn't change
    print(m)
    # all basic types (strings, ints, etc.) use pass by value: copy of variable is created passed into function
    
# every function I write will have a docstring
def sum_two_ints(a:int, b:int) -> int:
    """
    Adds two integers and returns their sum.
    
    Parameters: 
    - a (int)
    - b (int)
    Returns:
    int: a+b
    """
    return a + b

def double_and_duplicate(a:float) -> tuple[float, float]: # tuples - grouping variables together
    """
    Double the input variable and return two copies of the result
    """
    return 2 * a, 2 * a

def print_hi():
    print("hi")
    
def add_one(k:int) -> int:
    """
    Add one to the input variable and return it"""
    return k + 1

if __name__ == "__main__":
    main()
def main():
    print("Conditionals in Python.")
    
    print("The min of 3 and 4 is", min_2(3, 4))
    print(which_is_greater(3, 4))
    
    
# comparison operators: >, <, >=, <=, ==

def positive_difference(a:int, b:int) -> int:
    """
    Takes two integers, returns their positive difference
    """
    if a > b:
        return a - b
    else:
        return b - a
    
def pd(a, b):
    return abs (a-b)

def same_sign(x: int, y: int) -> bool:
    """
    Takes integers x, y as input and returns True if they have the same sign, False otherwise.
    Zero is considered to have the same sign as all integers.
    """
    return (x >= 0 and y >= 0) or (x <= 0 and y <= 0)

def same_sign_faster(x: int, y: int) -> bool:
    """
    Takes integers x, y as input and returns True if they have the same sign, False otherwise.
    """
    return x * y >= 0
    
def which_is_greater(x: int, y: int) -> int:
    """
    Takes two ints as input and returns 1 if x > y, -1 if y > x, and 0 if they're equal
    """
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1
    
# Note: Python has a build in function min() that takes min of any # of numbers
def min_2(a: int, b: int) -> int:
    """
    Takes two integers as input and returns their min.
    """
    if a < b:
        return a
    # if I make it here, I know b <= a
    return b


if __name__ == "__main__":
    main()
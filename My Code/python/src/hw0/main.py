
def main():
    print(next_perfect_number(8128))

def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative).
        k: Number of positions to fill (non-negative).
    Returns:
        The number of ways to choose and order k items from n, i.e., P(n, k).
    """
    product = 1
    for i in range(0, k):
        product *= n-i
    return product

def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    k_factorial = 1
    for i in range(1, k+1):
        k_factorial *= i
    n_permute_k = 1
    for j in range(0, k):
        n_permute_k *= n-j
    
    n_choose_k = int(n_permute_k / k_factorial)
    return n_choose_k

# Insert your power() function here, along with any subroutines that you need.
def power(a: int, b: int) -> int:
    """
    Compute a raised to the b-th power.
    Args:
        a: Base integer (can be negative, zero, or positive).
        b: Exponent integer (must be non-negative).
    Returns:
        The integer value of a^b. By convention, 0^0 returns 1.
    """
    product = 1
    for i in range(1, b+1):
        product = product * a
    return product

# Insert your sum_proper_divisors() function here, along with any subroutines that you need.
def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    Args:
        n: Integer input.
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    Args:
        n: A non-negative integer.
    Returns:
        A list F of length n + 1 such that F[k] is the k-th Fibonacci number.
    """
    fibonacci_nums = [1] * (n + 1)
    for i in range(2, n + 1):
        fibonacci_nums[i] = fibonacci_nums[i - 1] + fibonacci_nums[i - 2]
    return fibonacci_nums

# Insert your divides_all() function here, along with any subroutines that you need.
def divides_all(a: list[int], d: int) -> bool:
    """
    Determine whether d divides every element of a.
    Args:
        a: A list of integers.
        d: The candidate divisor.
    Returns:
        True if every element x in a satisfies x % d == 0.
        False immediately if d == 0, since zero is not a divisor of any number.
    """
    if d == 0:
        return False
    for i in range(len(a)):
        if a[i] % d != 0:
            return False
    return True

# Insert your max_integer_array() function here, along with any subroutines that you need.
def max_integer_array(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    max = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

def max_integers(*numbers: int) -> int:
    """
    Return the maximum integer among a variable number of inputs.
    Args:
        numbers: One or more integers.
    Returns:
        The largest integer in numbers.
    Raises:
        ValueError: If no numbers are provided.
    """
    if(len(numbers) == 0):
        raise ValueError("numbers can't be empty")
    return max_integer_array(numbers)

# Insert your sum_integers() function here, along with any subroutines that you need.
def sum_integers(*numbers: int) -> int:
    """
    Return the sum of a variable number of integers.
    Args:
        numbers: Zero or more integers.
    Returns:
        The sum of all provided integers. Returns 0 if no arguments are given.
    """
    sum = 0
    for i in range(0, len(numbers)):
        sum += numbers[i]
    return sum

# Insert your gcd_array() function here, along with any subroutines that you need.
# Insert your max_integers() function here, along with any subroutines that you need.
def homogenous_array(lst: list[int]) -> bool:
    element0 = lst[0]
    for element in lst:
        if element != element0:
            return False
    return True
        
def min_integer_index(lst: list[int]) -> int:
    """
    Return the maximum integer in a non-empty list.
    Args:
        lst: A non-empty list of integers.
    Returns:
        The largest integer in lst.
    """
    index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[0]:
            index = i
    return index

def gcd_array(a: list[int]) -> int:
    """
    Return the greatest common divisor (GCD) of all integers in the list.
    Args:
        a: A non-empty list of integers (values may be negative or zero).
    Returns:
        The non-negative GCD of all numbers in `a`. 
    """
    while(homogenous_array(a) == False):
        min_int_index = min_integer_index(a)
        for i in range(len(a)):
            if(a[i] != a[min_int_index]):
                a[i] -= a[min_int_index]
    return a[0]

# Insert your is_perfect() function here, along with any subroutines that you need.
def is_perfect(n: int) -> bool:
    """
    Determine whether an integer n is a perfect number.
    Args:
        n: Integer to test.
    Returns:
        True if n is perfect, False otherwise.
    """
    sum = 0
    for i in range(1, n): # determine the factors of n
        if n % i == 0:
            sum += i
    return sum == n

def next_perfect_number(n: int) -> int:
    """
    Return the smallest perfect number strictly greater than n.
    Args:
        n: Integer threshold.
    Returns:
        The least perfect number > n.
    """
    n += 1
    while(not is_perfect(n)):
        n += 1
    return n


import math
def is_prime(n: int) -> bool:
    """
    Test if n is prime.
    Parameters:
    - n (int): an integer
    Returns:
    bool: True if n is prime and False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
             return False
    return True        

# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:;
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    mersenne_prime_list = []
    for p in range (1, n+1):
        test_value = int(math.pow(2, p) - 1)
        if(is_prime(test_value)):
            mersenne_prime_list.append(test_value)
    return mersenne_prime_list

if __name__ == "__main__":
    main()
def main():
    print("While Loops!")
    print(factorial(5))
    print(factorial_v2(5))
    print(sum_first_n_integers_v2(100))
    
def sum_first_n_integers(n: int) -> int:
    """
    Takes as input an integer n and returns sum of the first n positive integers, n + (n-1) +...+ 2 + 1
    """
    if n < 0:
        print("n is", n)
        raise ValueError("Error: negative input given to factorial")
    tracker = n - 1
    while (tracker > 0):
        n += tracker
        tracker -= 1
    return n

def gauss_sum(n: int) -> int:
    return n * (n + 1) // 2 # integer division

def sum_first_n_integers_v2(n: int) -> int:
    """
    Takes as input an integer n and returns sum of the first n positive integers, n + (n-1) +...+ 2 + 1
    """
    s = 0
    j = 1
    while(j <= n):
        s += j
        j += 1
    
def factorial(n: int) -> int:
    """
    Take as input an integer n, return n!
    """
    if n < 0:
        print("n is", n)
        raise ValueError("Error: negative input given to factorial")
    product = 1
    i = 1
    while (i <= n):
        product *= i
        i += 1 # sometimes hard of answering question: infinite loop or taking long time doing good work 
    return product

def factorial_v2(n: int) -> int:
    if n < 0:
        print("n is", n)
        raise ValueError("Error: negative input given to factorial")
    tracker = n - 1
    while (tracker > 0):
        n *= tracker
        tracker -= 1
    return n

if __name__ == "__main__":
    main()
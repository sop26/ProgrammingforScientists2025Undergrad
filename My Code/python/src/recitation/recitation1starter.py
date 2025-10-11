import math
from primes.main import sieve_of_eratosthenes
import matplotlib.pyplot as plt


def prime_count_array(n: int):
    #TODO Implement this function
    """
    input: an integer n
    output: list of primes we've seen so far at a given index
    """
    prime_list = sieve_of_eratosthenes(n)
    counter = 0
    result = [0] * n
    for i in range(len(result)):
        if prime_list[i]:
            counter += 1
        result[i] = counter
    return result

def prime_count_array_plotting():
    N = 200000
    pi = prime_count_array(N)
    # Sample points to keep plotting light
    step = 100
    xs = list(range(2, N + 1, step))
    ys = [pi[x] for x in xs]    
    ys_approx = [x / math.log(x) for x in xs] # n/log n approximation
    # Plot
    plt.figure(figsize=(9, 6))
    plt.plot(xs, ys, label=r"$\pi(n)$ (prime count)")
    plt.plot(xs, ys_approx, linestyle="--", label=r"$n/\log n$ (approximation)")
    plt.title("Prime Counting Function $\\pi(n)$ vs. $n$ (with $n/\\log n$ approximation)")
    plt.xlabel("n")
    plt.ylabel(r"$\pi(n)$")
    plt.legend()
    plt.tight_layout()
    plt.show()

def ulam_coords(n: int):
    coords = [(0, 0)] * n
    x = y = 0
    k = 1
    step_len = 1

    def write_and_step(dx, dy, steps, k, x, y):
        for _ in range(steps):
            if k > n:
                break
            coords[k - 1] = (x, y)
            x += dx
            y += dy
            k += 1
        return k, x, y
    while k <= n:
        # right, up
        k, x, y = write_and_step(1, 0, step_len, k, x, y)
        k, x, y = write_and_step(0, 1, step_len, k, x, y)
        step_len += 1
        # left, down
        k, x, y = write_and_step(-1, 0, step_len, k, x, y)
        k, x, y = write_and_step(0, -1, step_len, k, x, y)
        step_len += 1
    return coords

def plot_ulam(n: int = 20000, point_size: float = 2.0):
    is_prime = sieve_of_eratosthenes(n)
    coords = ulam_coords(n)
    xs = []
    ys = []
    for k in range(2, n + 1): # start at 2 (first prime)
        if is_prime[k]:
            x, y = coords[k - 1]
            xs.append(x)
            ys.append(y)
    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, s=point_size)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.title(f"Ulam Spiral of Primes up to {n}")
    plt.show()
    plt.close()


def main():
    prime_count_array_plotting()
    # plot_ulam(n=30000, point_size=1.8)
    

    
if __name__ == "__main__":
    main()
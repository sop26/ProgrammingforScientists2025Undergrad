import random 
import multiprocessing
import time

def main():
    print(estimate_pi_multi_procs(100000, 5))
    
def estimate_pi_partial(num_trials: int, result_queue: multiprocessing.Queue) -> None:
    """
    Performs a partial Monte Carlo estimation of π by randomly sampling points
    within the unit square and counting how many fall inside the unit circle.

    Args:
        num_trials (int): Number of random (x, y) points to generate, where
            x and y are in [0, 1).
        result_queue (multiprocessing.Queue): Shared queue for returning the
            count of points that land inside the unit circle.

    Returns:
        None: This function does not return a value directly but places the
        count of successful points (inside the circle) into the result_queue.
    """
    inside_count = 0

    for _ in range(num_trials):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside_count += 1

    # Send the number of inside-circle hits back to the parent process
    result_queue.put(inside_count)


def estimate_pi_multi_procs(num_points : int, num_procs: int) -> float: 
    """
    Estimates the value of pi by sampling from num_points and using multiple processors.

    Input:
        num_points (int): The number of random points to sample from 
        num_procs (int): The number of processors (processes) to use.

    Output:
        float: The estimated value of pi
    """
    chunk = num_points // num_procs
    result_queue = multiprocessing.Queue()
    processes = []
    for i in range(num_procs):
        if i == num_procs - 1:
            num_slice = chunk + num_points % num_procs
        else:
            num_slice = chunk
        p = multiprocessing.Process(target = estimate_pi_partial, args = (num_slice, result_queue))
        p.start()
        processes.append(p)
        
    for p in processes:
        p.join()
    
    total = 0
    for i in range(num_procs):
        total += result_queue.get()

    return 4 * total/num_points

if __name__ == "__main__":
    main()
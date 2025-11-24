import time
import random
import multiprocessing 

def main():
    print("Parallel programming and craps.")
    num_procs = multiprocessing.cpu_count()
    num_trials = 1000
    start_parallel = time.time()
    house_edge = compute_craps_house_edge_parallel(num_trials, num_procs)
    end_parallel = time.time()
    total_parallel = end_parallel - start_parallel
    print(f"Time taken for parallel: {total_parallel}")
    
    start_serial = time.time()
    house_edge = compute_craps_house_edge_serial(num_trials)
    end_serial = time.time()
    total_serial = end_serial - start_serial
    print(f"Time taken for serial: {total_serial}")
    
    


def roll_die() -> int:
    """Simulate rolling a single six-sided die."""
    return random.randint(1, 6)

def sum_dice(num_dice: int) -> int:
    """Simulate rolling num_dice six-sided dice and summing the results."""
    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total

def play_craps_once() -> bool:
    """
    Simulate a single game of craps.
    Return True if player wins, False if loses.
    """
    first_roll = sum_dice(2)
    if first_roll == 7 or first_roll == 11:
        return True
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    else:
        while True:
            next_roll = sum_dice(2)
            if next_roll == first_roll:
                return True
            elif next_roll == 7:
                return False

def compute_craps_house_edge_serial(num_trials: int) -> float:
    """
    Simulate num_trials games of craps in serial.
    """
    win_total = 0
    for _ in range(num_trials):
        if play_craps_once():
            win_total += 1
        else:
            win_total -= 1
    return win_total / num_trials

def compute_craps_house_edge_parallel(num_trials: int, num_procs: int) -> float:
    """
    Simulate num_trials games of craps in parallel, divided over num_procs worker processes, and return the house edge of the game
    """
    win_total = 0
    result_queue = multiprocessing.Queue()
    processes = []
    trials_one_proc = num_trials // num_procs
    
    for i in range(num_procs):
        if i == num_procs - 1:
            trials = trials_one_proc + num_trials % num_procs
        else:
            trials = trials_one_proc
        p = multiprocessing.Process(target = total_win_one_proc, args = (trials, result_queue))
        p.start()
        processes.append(p)
        
    for p in processes:
        p.join()
    
    win_total = 0   
    for i in range(num_procs):
        win_total += result_queue.get()
           
    return win_total/num_trials
        
def total_win_one_proc(num_trials, result_queue: multiprocessing.Queue) -> None:
    """
    One worker bee playing craps num_trials_one_proc times.
    """
    win_total = 0
    for _ in range(num_trials):
        if play_craps_once():
            win_total += 1
        else:
            win_total -= 1
    result_queue.put(win_total)
    


if __name__ == "__main__":
    main()

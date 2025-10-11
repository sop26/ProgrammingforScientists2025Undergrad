
"""
Pseudocode (from Learning Objectives)

RollDie()
    roll ← RandIntn(6)
    return roll + 1

PlayCrapsOnce()
    numDice ← 2
    firstRoll ← SumDice(numDice)
    if firstRoll = 2, 3, or 12
        return false (player loses)
    else if firstRoll = 7 or 11
        return true (player wins)
    else
        while true
            newRoll ← SumDice(numDice)
            if newRoll = firstRoll 
               return true
            else if newRoll = 7
                return false

ComputeCrapsHouseEdge(numTrials)
    count ← 0
    for numTrials total trials
        outcome ← PlayCrapsOnce()
        if outcome = true
            count ← count + 1
        else
            count ← count − 1
    return count/numTrials

Built-in PRNG references
- RandIntn(n)  → Python: random.randrange(a, b) returns integer in [a, b-1]
- RandFloat()  → Python: random.random() returns float in [0, 1) - Python can only represent finitely many numbers
"""

import random # allows pseudorandom number generation
import time


def main():
    print("Rolling dice and playing craps.")
    # random.seed(0) # default for some history of Python
    # random.seed(time.time_ns) # now this is what runs behind the scenes
    num_trials = 1000
    edge = compute_craps_house_edge(num_trials)
    print(f"Estimated house edge with {num_trials} trials is: {edge:.6f}")
    # initial_stuff()
    

def initial_stuff():
    print(random.randrange(0, 10)) # 0 to 9 inclusive
    print(random.random()) # [0, 1) this is faster than just pulling from time every single time
    print(random.random())
    for _ in range(10):
        print("Die roll: ", roll_die())
    for _ in range(10):
        print("Rolling two dice gives:", sum_dice(2))


def roll_die() -> int:
    """
    Simulates the roll of a die.
    Returns:
    - int: A pseudorandom integer between 1 and 6, inclusively.
    """
    # TODO: Implement this function
    return random.randrange(1, 7)
# 3 functions
# 1. generate random int (Python doesn't have support for this)
# 2. generate random int in a rnage [0, n)
# 3. generate float in range [0, 1]

# def sum_two_dice() -> int:
#     num = random.random()
#     if num < 1.0/36.0:
#         return 2
#     elif num < 3.0/36.0: #[1/36, 3/36]
#         return 3
#     elif num < 6.0/36.0:
#         return 4

def sum_dice(num_dice: int) -> int:
    """
    Simulates the process of summing n dice.
    Parameters:
    - num_dice (int): The number of dice to sum.
    Returns:
    - int: The sum of num_dice simulated dice.
    """
    if num_dice <= 0:
        raise ValueError("num_dice must be a positive integer.")
    total = 0
    for _ in range(num_dice):
        total += roll_die()
    return total


def play_craps_once() -> bool:
    """
    Simulates one game of craps.
    Returns:
    - bool: True if the game is a win, False if it's a loss.
    """
    # TODO: Implement this function
    dice_sum = sum_dice(2)
    if dice_sum == 7 or dice_sum == 11: #6/36 + 2/36 = 8/36
        return True
    elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12: #1/36 + 2/36 + 1/36 = 4/36
        return False
    else: # 24/36, x = 7/36 vs x < 7/36
        # new_dice_sum = sum_dice(2)
        # while new_dice_sum != 7 or new_dice_sum != dice_sum: # alternatively can just do a return true
        while True:
            new_dice_sum = sum_dice(2)
            if new_dice_sum == 7:
                return False
            elif new_dice_sum == dice_sum:
                return True

def compute_craps_house_edge(num_trials: int) -> float:
    """
    Estimates the "house edge" of craps over multiple simulations.
    Parameters:
    - num_trials (int): The number of simulations.
    Returns:
    - float: The house edge of craps (average amount won or lost per game, per unit bet).
    Positive means player profit; negative means house profit.
    """
    if num_trials <= 0:
        raise ValueError("num_trials must be a positive integer.")
    count = 0
    for _ in range(num_trials):
        if play_craps_once():
            count += 1
        else:
            count -= 1     
    return count/num_trials # avg outcome over all trials

if __name__ == "__main__":
    main()

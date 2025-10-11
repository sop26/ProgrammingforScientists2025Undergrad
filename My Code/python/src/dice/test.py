import random # this should be helpful!

def main():
    print(average_game_length(10000))
def average_game_length(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and estimate the average number 
    of dice rolls per game.

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: The estimated average number of dice rolls per game.
    """
    total_count = 0
    for _ in range(num_trials):
        sum_dice = random.randrange(1, 7) + random.randrange(1, 7)
        print(sum_dice)
        dice_roll_count = 1
        if sum_dice == 7 or sum_dice == 11 or sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
            total_count += 1
        else:
            while(True):
                new_sum_dice = random.randrange(1, 7) + random.randrange(1, 7)
                dice_roll_count += 1
                if new_sum_dice == sum_dice or new_sum_dice == 7:
                    total_count += dice_roll_count
                    break
    return float(total_count) / float(num_trials)

if __name__ == "__main__":
    main()
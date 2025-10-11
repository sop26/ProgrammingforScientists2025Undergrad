import random  # for generating random numbers
from election_io import read_electoral_votes, read_polling_data 

def main():
    print("Let's simulate an election!")
    electoral_vote_file = "data/electoralVotes.csv"
    polling_file = "data/conventions.csv"
    electoral_votes = read_electoral_votes(electoral_vote_file)
    polling_data = read_polling_data(polling_file)
    print("Data read!")
    num_trials = 1000000
    margin_of_error = 0.05
    probability_1, probability_2, probability_tie = simulate_multiple_elections(polling_data, electoral_votes, num_trials, margin_of_error)
    print("Election simulated!")
    print("Probability of candidate 1 winning: ", probability_1)
    print("Probability of candidate 2 winning: ", probability_2)
    print("Probability of tie: ", probability_tie)

def simulate_multiple_elections(polls: dict[str, float], electoral_votes: dict[str, int], num_trials: int, margin_of_error: float) -> tuple[float, float, float]: 
    """
    Simulates an election multiple times, calculating winning probabilities
    
    Parameters:
    - polls: maps state names to candidate 1 percentages
    - electoral_votes: maps state names to electoral college votes
    - num_trials: number of trials to simulate
    - margin of error: margin of error of each poll
    
    Returns:
    - tuple of 3 floats corresponding to winning percentages of candidate 1, candidate 2, and a tie
    """
    if num_trials <= 0:
        raise ValueError("Number of trials must be positive.")
    if margin_of_error <= 0:
        raise ValueError("Margin of error must be non-negative.")
    
    win_count_1 = 0
    win_count_2 = 0
    tie_count = 0
    
    # sims go here
    
    for _ in range(num_trials):
        # number of EC votes for candidate 1 and 2
        votes_1, votes_2 = simulate_one_election(polls, electoral_votes, margin_of_error)
        if votes_1 > votes_2:
            win_count_1 += 1
        elif votes_2 > votes_1:
            win_count_2 += 1
        else:
            tie_count += 1
    
    probability_1 = win_count_1/ num_trials
    probability_2 = win_count_2/num_trials
    probability_tie = tie_count/num_trials
    
    return probability_1, probability_2, probability_tie
    
def simulate_one_election(polls: dict[str, float], electoral_votes: dict[str, int], margin_of_error: float) -> tuple[int, int]:
    """
    Simulates one presidential election between two candidates using polling data and returns the # of electoral colleg evotes for each candidate.
    
    Parameters:
    - polls: maps state names to candidate 1 percentages
    - electoral_votes: maps state names to electoral college votes
    - margin of error: margin of error of each poll
    
    Returns:
    - tuple of 2 integers corresponding to number of electoral votes for candidate 1 and candidate 2, respectively, after one simulation
    """
    if margin_of_error < 0:
        raise ValueError("MOE can't be negative.")
    
    college_votes_1 = 0
    college_votes_2 = 0
    for state_name, polling_value in polls.items():
        adjusted_polling_value = add_noise(polling_value, margin_of_error)
        num_votes = electoral_votes[state_name]
        
        if adjusted_polling_value > 0.5:
            college_votes_1 += num_votes
        else: # odds == 0.5 very unlikely
            college_votes_2 += num_votes
    return (college_votes_1, college_votes_2)
        
def add_noise(polling_value: float, margin_of_error: float) -> float: 
    """
    Adds random noise to a polling avlue.
    
    Parameters:
    - polling_value (float): The polling value for candidate 1.
    - margin_of_error (float): The margin of error for this poll.
    
    Returns:
    - float: The adjusted polling value after assigning some noise for candidate 1 with given margin of error
    """
    # x = random.gauss(0,1)
    # x/=2.0
    # x*= margin_of_error
    # polling_value += x
    # margin of error is 2 x the standard_deviation. standard deviation is margin of error/ 2
    st_dev = 0.5 * margin_of_error
    x = random.gauss(0, st_dev)
    return polling_value + x
    
if __name__ == "__main__":
    main()
def main():
    print("Dictionaries in Python (aka maps).")
    polls = {} # empty dictionary
    
    polls: dict[str, float] = {
        "Pennsylvania" : 0.517
    }
    # can set value associated with any key
    # polls["Pennsylvania"] = 0.517
    polls["Ohio"] = 0.488
    polls["Texas"] = 0.378
    polls["Florida"] = 0.5
    
    print("num states", len(polls))
    
    if "Florida" in polls:
        del polls["Florida"]
    print("num states after florida deletion", len(polls))
    
    electoral_votes: dict[str, int]= {
        "Pennsylvania": 20,
        "Ohio": 18,
        "Texas": 38
    }
    update_votes(electoral_votes) # lists are passed by reference
    print(electoral_votes)
    
    for state_name in electoral_votes: # when range of dict, get key
        print("The number of electoral votes in", state_name, "is", electoral_votes[state_name])
    
    # we also have double ranging for dictionaries
    for state_name, votes in electoral_votes.items(): # basically like how have to enumerate for lists 
        print("The number of electoral votes in", state_name, "is", votes)
    
    # let's instead get these in alphabetical order. but how? Python gives us an operator dict.keys() that produces of all keys which we can convert to a list
    state_names = list(electoral_votes.keys())
    state_names.sort()
    print(state_names)
    
    for state in state_names:
        print("The number of electoral votes in", state, "is", electoral_votes[state])
    
def update_votes(votes: dict[str, int]) -> None:
    votes["Pennsylvania"] = 19
    votes["Ohio"] = 17
    votes["Texas"] = 40
    
if __name__ == "__main__":
    main()
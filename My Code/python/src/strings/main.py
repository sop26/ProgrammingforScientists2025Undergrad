
def main():
    print("String in Python.")
    s = "Hi"
    t = 'Lovers'
    # strings can have single or double quotes (unlike java, etc)
    
    u = s+ " " + t
    print(u)
    print(s*3) # multiplication is repeated concatenation
    
    # access symbols of a st ring like we do elements of a tuple/list
    print("The first symbol of u is", u[0])
    print("The final symbol is", u[len(u)- 1])
    
    if t[2] == "V":
        print("Third symbol of t is v.")
        
    #HiLovers to HiLosers
    # u[4] = "s" # doesn't work :(). strings, like tuples, are immutable
    s = "Yo"
    s += "-Yo"
    s+= " Ma"
    
    print(s)
    
    dna = "ACGTAC"
    print(complement(dna))
    print(reverse(dna))
    print(reverse_complement(dna))
    
    
def complement(dna: str) -> str:
    """
    Finds the complementary strand of a given DNA string.
    """
    complementary_strand = ""
    for symbol in dna:
        match symbol:
            case "A":
                complementary_strand += "T"
            case "C":
                complementary_strand += "G"
            case "T":
                complementary_strand += "A"
            case "G":
                complementary_strand += "C"
            case _: # anything else
                raise ValueError("Invalid symbol given.")
    return complementary_strand
            
def reverse(dna: str) -> str:
    reversed_strand = ""
    for i in range(len(dna)-1, -1, -1):
        reversed_strand += dna[i]
    return reversed_strand

def reverse_complement(dna: str) -> str:
    """
    Takes a DNA string as input and returns its reverse complement
    """
    return reverse(complement(dna))    
# modularity
"""
ReverseComplement(pattern)
    pattern <- Reverse(pattern)
    pattern <- Complement(pattern)
    return pattern
"""    
    
if __name__ == "__main__":
    main()
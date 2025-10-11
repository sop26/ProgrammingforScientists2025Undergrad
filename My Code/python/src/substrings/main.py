def main():
    s = "Hi Lovers"
    print(s[1:5])
    print(s[:7]) # if first index is omitted, it's zero
    print(s[4:]) # if final index is omitted, it's len(s)
    print(pattern_count("aaa", "aaatttaaa"))
    print(starting_indices("aaa", "aaatttaaa"))
    
    # exact same notation applies to sublists (not just strings)
    
def pattern_count(pattern: str, text:str) -> int:
    """
    Find the number of times the substring occurs in the larger text, including overlaps
    """
    return len(starting_indices(pattern, text))
# finding starting indices is a more general problem than counting # of indices
def starting_indices(pattern: str, text: str) -> list[int]:
    indices = []
    pattern_size = len(pattern)
    text_size = len(text)
    if pattern_size == 0:
        raise ValueError("empty pattern not allowed")
    if pattern_size > text_size:
        return 0
    for i in range(0, text_size-pattern_size+1):
        if text[i:i + pattern_size] == pattern:
            indices.append(i)
    return indices
    
if __name__ == "__main__":
    main()
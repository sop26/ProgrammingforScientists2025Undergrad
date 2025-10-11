def main():
    print("Two-dimensional array (tuples and lists).")
    
    # here is a mystery 3x3 matrix from HW 3
    # 2-d tuple whose elements are tuples
    kernel = (
        (0.05, 0.20, 0.05),
        (0.20, 0, 0.20),
        (0.05, 0.20, 0.05)
    )
    print(kernel)
    print(kernel[0][1])
    # tuples are immutable
    
    a = [[0] * 4] * 7
    a[1][3] = 5
    # we created only one list of length 4 and we created 7 references to it
    
    a = []
    for row in range(7):
        new_row = [0] * 4
        a.append(new_row)
        
    for r in range(7):
        print(a[r])
    print("Num of rows is", len(a)) 
    print("Num of columns is", len(a[0])) 
        
    num_rows = len(a)
    board = []     
    for row in range(num_rows):
        current_row = [False] * row
        board.append(current_row)
        
    print(board)
        
    # let's add a False element to each row
    for row in range(len(board)): 
        board[row].append(False)
        
    print(board) 
       
    set_first_element_to_true(board)
    print("I tried to set the top left element to True.")

def set_first_element_to_true(a: list[list[bool]]) -> None:
    """
    Set the top left element of a 2-D boolean list to True
    """
    if len(a) == 0 or len(a[0] == 0):
        raise ValueError("Board is empty or has no first row length")
    a[0][0] = True

def play_game_of_life_board(board: list[list[bool]]) -> list[list[list[bool]]]:
    

if __name__ == "__main__":
    main()
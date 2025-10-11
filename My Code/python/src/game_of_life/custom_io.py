from datatypes import GameBoard
from functions import assert_rectangular


def read_board_from_file(filename: str) -> GameBoard:
    """
    Reads a CSV file representing a Game of Life board.
    "1" = alive (True), "0" = dead (False).
    Args:
        filename (str): The name of the CSV file.
    Returns:
        GameBoard: Parsed board.
    """
    if not isinstance(filename, str) or len(filename) == 0:
        raise ValueError("filename must be a non-empty string.")
    # open(filename, 'r') as f: opens the file with name filename in read mode ('r') and returns a file object called f
    
    giant_string = ""
    
    with open(filename, 'r') as f:
        # adding "with" means that as soon as this block finishes, the file is closed
        giant_string = f.read() # read file and return giant string of file contents
        
    trimmed_giant_string = giant_string.strip() # trim whitespace
    # split the string into multiple strings, one for each line
    lines = trimmed_giant_string.splitlines()
    num_rows = len(lines)
    
      # how do I make a GameBoard?
    board: GameBoard = []

    # now we read through the lines, and parse each line to add to our board 

    for current_line in lines:
        # split the current line every time we see a comma 
        line_elements = current_line.split(',')

        # line_elements is a list of strings, one string for each element in the current line (commas not included)

        # set the row values with a subroutine 
        new_row = set_row_values(line_elements)

        # new_row is a 1D list of booleans that we can append to board 
        board.append(new_row)

        
    assert_rectangular(board)
        
    return board


def set_row_values(line_elements: list[str]) -> list[bool]:
    """
    Convert a list of "0"/"1" strings into booleans.
    Args:
        line_elements (list[str]): Strings "0"/"1".
    Returns:
        list[bool]: Row with True/False.
    """
    if not isinstance(line_elements, list) or len(line_elements) == 0:
        raise ValueError("line_elements must be a non-empty list.")
    
    current_row = []
    for element in line_elements:
        if element == "0":
            current_row.append(False)
        elif element == "1":
            current_row.append(True)
        else:
            raise ValueError("Error: invalid entry in board file.")
    return False

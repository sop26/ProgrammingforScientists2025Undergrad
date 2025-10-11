# Insert your simulate_gray_scott() function here, along with any subroutines that you need.
# Sophie Li 10/9/25

import sys
import math
from decimal import Decimal

def total_concentration(board: list[list[tuple[float, float]]]):
    total_A = 0
    total_B = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            total_A += board[row][col][0]
            total_B += board[row][col][1]
    return (total_A, total_B)

def initialize_board(num_rows: int, num_cols: int):
    new_board = []
    for _ in range(num_rows):
        new_board.append([0] * num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            new_board[i][j] = [0.0, 0.0]
    return new_board

def simulate_gray_scott(initial_board: list[list[tuple[float, float]]], num_gens: int, feed_rate: float, kill_rate: float, prey_diffusion_rate: float, predator_diffusion_rate: float, kernel: list[list[float]]) -> list[list[list[tuple[float, float]]]]:
    """
    Simulates the Gray-Scott model
    
    Parameters: 
        initial_board: the starting board
        num_gens: number of generations
        feed_rate: the rate at which A is fed into the system
        kill_rate:the rate at which B is killed
        prey_diffusion_rate: the scalar used for convolution on the Moore neighborhood of A
        predator_diffusion_rate: the scalar used for convolution on the Moore neighborhood of B
        kernel: the fixed matrix to take the convolution of
        
    Return:
        a list of num_gen boards for the simulation
    """
    boards = []
    boards.append(initial_board)
    for i in range(num_gens):
        boards.append([0] * len(initial_board))

    for i in range(1, num_gens + 1):
        boards[i] = update_board(boards[i-1], feed_rate, kill_rate, prey_diffusion_rate, predator_diffusion_rate, kernel)
    return boards

def update_board(current_board: list[list[tuple[float, float]]], feed_rate: float, kill_rate: float, prey_diffusion_rate: float, predator_diffusion_rate: float, kernel: list[list[float]]) -> list[list[tuple[float, float]]]:
    """
    Updates the board by updating each cell
    
    Parameters: 
        current_board: the board of interest
        feed_rate: the rate at which A is fed into the system
        kill_rate:the rate at which B is killed
        prey_diffusion_rate: the scalar used for convolution on the Moore neighborhood of A
        predator_diffusion_rate: the scalar used for convolution on the Moore neighborhood of B
        kernel: the fixed matrix to take the convolution of
        
    Return:
        a board that is a list of list of tuples 
    """
    num_rows = len(current_board)
    num_cols = len(current_board[0])
    new_board = []
    for i in range(num_rows):
        new_board.append([0] * num_cols)
    for row in range(num_rows):
        for col in range(num_cols):
            new_board[row][col] = update_cells(current_board, row, col, feed_rate, kill_rate, prey_diffusion_rate, predator_diffusion_rate, kernel)
    return new_board
    
def update_cells(current_board: list[list[float]], row: int, col: int, feed_rate: float, kill_rate: float, prey_diffusion_rate: float, predator_diffusion_rate: float, kernel: list[list[float]]) -> tuple[float, float]:
    """
    Updates the cell at the specified row and column based on reactions and diffusion
    
    Parameters: 
        current_board: the board of interest
        row: row of cell to update
        col: column of cell to update
        feed_rate: the rate at which A is fed into the system
        kill_rate:the rate at which B is killed
        prey_diffusion_rate: the scalar used for convolution on the Moore neighborhood of A
        predator_diffusion_rate: the scalar used for convolution on the Moore neighborhood of B
        kernel: the fixed matrix to take the convolution of
        
    Return:
        a cell that is a tuple containing concentration of A and concentration of B
    """
    reaction_change = change_due_to_reactions(current_board[row][col], feed_rate, kill_rate)
    diffusion_change = change_due_to_diffusion(current_board, row, col, prey_diffusion_rate, predator_diffusion_rate, kernel)

    new_cell = sum_cells(current_board[row][col], reaction_change, diffusion_change)
    return (new_cell[0], new_cell[1])

def sum_cells(*cells: list[tuple[float, float]]) -> tuple[float, float]:
    """
    Sums up the concentration of A and the concentration of B for each cell
    
    Parameters:
        cells: a list of cells each containing a concentration A and B
        
    Returns:  
        a tuple containing the sum of concentration A and the sum of concetration B
    """
    sum_A = 0
    sum_B = 0
    for cell in cells:
        sum_A += cell[0]
        sum_B += cell[1]
        
    return (sum_A, sum_B)

def change_due_to_reactions(current_cell: tuple[float, float], feed_rate: float, kill_rate: float) -> tuple[float, float]:
    """
    Computes the change in concentration of A and B due to reactions (feeding in A, killing B, A + 2B -> 3B)
    
    Parameters:
        the cell to compute changes off of
        the rate of feeding in A
        the rate of killing B
    Returns:
        a tuple with the change in concentration of A and B
    """
    delta_A = feed_rate * (1 - current_cell[0])
    delta_B = - kill_rate * current_cell[1]
    
    delta_A -= current_cell[0] * current_cell[1]**2
    delta_B += current_cell[0] * current_cell[1]**2
    
    return (delta_A, delta_B)

def change_due_to_diffusion(current_board: list[list[tuple[float, float]]], row: int, col: int, prey_diffusion_rate: float, predator_diffusion_rate: float, kernel: list[list[tuple[float, float]]]) -> tuple[float, float]:
    """"
    Computes the next board by doing a matrix convolution.
    
    Parameters: 
        current_board: the board of interest
        row: the row of the cell of interest
        col: the column of the cell of interest
        prey_diffusion_rate: the scalar used for convolution on the Moore neighborhood of A
        predator_diffusion_rate: the scalar used for convolution on the Moore neighborhood of B
        kernel: the fixed matrix to take the convolution of
        
    Return:
        a tuple containing the sum of change in concentration A and the sum of change in concentration B
    """
    conv_sum_A = prey_diffusion_rate * convolution_sum(current_board, row, col, kernel, 0)
    conv_sum_B = predator_diffusion_rate * convolution_sum(current_board, row, col, kernel, 1)
    return (conv_sum_A, conv_sum_B)
     
def convolution_sum(current_board: list[list[float, float]], row: int, col: int, kernel: list[list[float]], index_AB: int) -> float:
    """
    Computes the convolution sum for one element of the current board
    
    Parameters:
        current_board: the board to compute the convolution on
        kernel: the fixed matrix to take the convolution of
        index_AB: the index indicating whether to take the convolution sum of A or B
        
    Return: 
        an integer corresponding to the resulting sum 
    """
    conv_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
                if in_field(current_board, row + i, col + j):
                    conv_sum += kernel[i+1][j+1] * current_board[row + i][col + j][index_AB]
    return conv_sum

def in_field(current_board: list[list[float]], row: int, col: int) -> bool:
    """
    Checks if an element with specified row and column are within the dimensions of the board
    
    Parameters:
        current_board: to check row and col against
        row: the row of the element to check
        col: the column of the element to check
    
    Return:
        a boolean corresponding to whether or not the element is in the board
    """
    max_row = len(current_board)
    max_col = len(current_board[0])
    if row >= 0 and row < max_row and col >= 0 and col < max_col:
        return True
    
    return False
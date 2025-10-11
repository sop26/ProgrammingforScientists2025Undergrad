import sys
import pygame
import numpy
import imageio
from custom_io import read_board_from_file
from functions import play_game_of_life
from drawing import draw_game_boards, draw_game_board


def pygame_surface_to_numpy(surface: pygame.Surface) -> numpy.ndarray:
    """
    Convert a Pygame Surface to a NumPy RGB image array.
    Returns:
        numpy.ndarray: Frame as (height, width, 3) array.
    """
    return None  # TODO: implement


def main():
    print("Coding the Game of Life!")
    pygame.init()
    
    r_pentomino = read_board_from_file("boards/rPentomino.csv")
    
    cell_width = 20
    
    surface = draw_game_board(r_pentomino, cell_width)
    
    print("we made the surface?")
    
    pygame.quit()
    
    filename = "output/rPentomino.png"
    
    pygame.image.save(surface, filename)
    
    print("image created")
    
    # when we type commandl ine args, tuple of strings is created - length of tuple is 1 more than # args because firsrt one always name of program
    
    pygame.quit()

    if len(sys.argv) != 5:
        raise ValueError("Usage: python main.py initial_board.csv output_prefix cell_width num_gens")

    input_csv = sys.argv[1]
    output_prefix = sys.argv[2] # where I draw animation
    cell_width = int(sys.argv[3]) 
    num_gens = int(sys.argv[4])

    print("Parameters read in successfully!")
    
    
    print("Read in the initial Game of Life board.")
    initial_board = read_board_from_file(input_csv)
    
    boards = play_game_of_life(initial_board, num_gens)
    
    surfaces = draw_game_boards(boards)
    
    print("Boards drawn to canvases")
    
    video_path = output_prefix + ".mp4"
    writer = imageio.get_writer(video_path, fps=10, codec="libx264", quality = 8)
    
    for surface in surfaces:
        frame = pygame_surface_to_numpy(surface)
        writer.append_data(frame)
        
    writer.close()
    print("Success!")

def pygame_surface_to_numpy(surface: pygame.Surface) -> numpy.ndarray:
    """
    Convert a pygame surface to a numpy RGB image array
    """
    return pygame.surfarray.array3d(surface).swapaxes(0, 1)

if __name__ == "__main__":
    main()

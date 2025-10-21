import os
import sys
import pygame
import numpy as np
import imageio.v2 as imageio  # imageio handles MP4 export

from datatypes import Board
from functions import simulate_gray_scott, initialize_board, total_concentration
from drawing import draw_boards


def pygame_surface_to_numpy(surface: pygame.Surface) -> np.ndarray:
    """
    Convert a Pygame Surface to a NumPy RGB image array.

    Returns:
        np.ndarray: The frame as (height, width, 3) uint8 RGB.
    """
    return pygame.surfarray.array3d(surface).transpose(1, 0, 2)


def main():
    print("Gray–Scott reaction–diffusion model")

    num_rows = 100
    num_cols = 100

    print("Parameters read in successfully!")

    pygame.init()

    # initialize empty board
    initial_board: Board = initialize_board(num_rows, num_cols)

    # how many predator rows and columns are there?
    frac = 0.05
    pred_rows = int(frac * num_rows)
    pred_cols = int(frac * num_cols)
    mid_row, mid_col = num_rows // 2, num_cols // 2

    # a little for loop to fill predators
    for r in range(mid_row - pred_rows // 2, mid_row + pred_rows // 2):
        for c in range(mid_col - pred_cols // 2, mid_col + pred_cols // 2):
            initial_board[r][c] = (initial_board[r][c][0], 1) # predators

    # make prey = 1 everywhere
    for i in range(len(initial_board)):
        for j in range(len(initial_board[i])):
            initial_board[i][j] = (1, initial_board[i][j][1])

    # parameters
    num_gens = 8000
    feed_rate = 0.039
    kill_rate = 0.10

    # kernel for diffusion
    kernel = np.array([
        [0.05, 0.2, 0.05],
        [0.2, -1.0, 0.2],
        [0.05, 0.2, 0.05],
    ])

    print("Starting simulation...")
    
    # tuning code below as an attempt to automate search for patterns but didn't quite work
    # if one color substantially greater than other in final board, adjust kill rate (or feed rate) to compensate and run sim again
    
    # TUNE = True
    # STEP_SIZE = 0.05
    
    # if TUNE:
    #     to_continue = True
    #     while to_continue:
    #         print("FINAL_FEED", feed_rate, "FINAL_KILL", kill_rate)
    #         boards = simulate_gray_scott(
    #             initial_board,
    #             num_gens,
    #             feed_rate,
    #             kill_rate,
    #             prey_diffusion_rate=0.2,
    #             predator_diffusion_rate=0.1,
    #             kernel=kernel,
    #         )
    #         final_board = boards[len(boards) - 1]
    #         total_A = total_concentration(final_board)[0]
    #         total_B = total_concentration(final_board)[1]
    #         print("NEW ROUND")
    #         print("total_B", total_B, "total_A", total_A)
    #         if total_B + total_A == 0:
    #             metric = 0.0
    #         else:
    #             metric = total_B / (total_B + total_A)
                
    #         if metric < 0.1 or metric > 0.9:
    #             print("metric", metric)
    #             updated_kill_rate = kill_rate + ((2 * metric - 1) * STEP_SIZE)
    #             if updated_kill_rate < 0:
    #                 feed_rate += (2 * metric - 1) * STEP_SIZE
    #             else:
    #                 kill_rate = updated_kill_rate
    #         else:
    #             to_continue = False
    # else:
    
    boards = simulate_gray_scott(
            initial_board,
            num_gens,
            feed_rate,
            kill_rate,
            prey_diffusion_rate=0.2,
            predator_diffusion_rate=0.1,
            kernel=kernel,
        )

    print("Simulation complete!")

    print("Drawing boards to file")

    # for visualization
    n = 100
    cell_width = 1

    surfaces = draw_boards(boards, cell_width, n)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"f_{feed_rate}k_{kill_rate}")
    print("Encoding video with imageio...")
    video_path = f"{output_file}.mp4"
    writer = imageio.get_writer(video_path, fps=10, codec="libx264", quality=8)

    for surf in surfaces:
        frame = pygame_surface_to_numpy(surf)
        writer.append_data(frame)

    writer.close()

    print(f"Video saved as {video_path}")

    pygame.quit()


if __name__ == "__main__":
    main()
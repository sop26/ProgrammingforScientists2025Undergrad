"""
CLI entry point for the gravity simulation.

Usage:
    python main.py <scenario_name> <num_gens> <time_step> <canvas_width> <drawing_frequency>

Example:
    python main.py jupiterMoons 2000 0.01 800 5

This will read:   data/jupiterMoons.txt
and write video:  output/jupiterMoons.mp4
"""

import sys
import os
import time
import pygame
import imageio
from custom_io import read_universe
from gravity import simulate_gravity
from drawing import animate_system, pygame_surface_to_numpy, draw_to_canvas, save_video_from_surfaces

def main():    
    if len(sys.argv) != 6:
        raise ValueError("Error: incorrect num of params")
    scenario = sys.argv[1] # butterfly or jupiter moons
    input_file = f"data/{scenario}.txt"
    video_path = f"output/{scenario}.mp4"
    
    num_gens = int(sys.argv[2])
    time_step = float(sys.argv[3])
    canvas_width = int(sys.argv[4])
    drawing_frequency = int(sys.argv[5]) # how frequently to draw
    
    initial_universe = read_universe(input_file)
    time_points = simulate_gravity(initial_universe, num_gens, time_step)
    
    surfaces = animate_system(time_points, canvas_width, drawing_frequency)
    save_video_from_surfaces(surfaces, video_path, fps=10, codec = "libx264", quality = 8)
    """
    Run the full pipeline:
      1) read universe from file
      2) simulate gravity for N generations
      3) render selected frames to pygame surfaces
      4) encode frames to an MP4 video
    """
    print("Let's simulate gravity!")

def initial_demo():
    canvas_width = 1500 # num pixels wide and tall
    universe = read_universe("data/butterfly.txt")
    surface = draw_to_canvas(universe, canvas_width)
    pygame.image.save(surface, "output/Butterfly.png")
    
    universe = read_universe("data/jupiterMoons.txt")
    surface = draw_to_canvas(universe, canvas_width)
    pygame.image.save(surface, "output/JupiterMoon.png")
    

if __name__ == "__main__":
    main()
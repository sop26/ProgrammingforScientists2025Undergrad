import imageio.v2 as imageio #hint: this might be helpful for rendering an MP4
#feel free to import any additional packages!

from datatypes import OrderedPair, Boid, Sky
from functions import simulate_boids
from drawing import animate_system, save_video_from_surfaces
import sys
import random
import math

def main():
    #Process your command-line arguments here
    if len(sys.argv) != 13:
        raise ValueError("Error: incorrect num of params")
    num_boids = int(sys.argv[1]) # butterfly or jupiter moons
    sky_width = float(sys.argv[2])
    initial_speed = float(sys.argv[3])
    max_boid_speed = float(sys.argv[4])
    num_gens = int(sys.argv[5])
    proximity = float(sys.argv[6])
    separation_factor = float(sys.argv[7])
    alignment_factor = float(sys.argv[8]) # how frequently to draw
    cohesion_factor = float(sys.argv[9])
    time_step = float(sys.argv[10])
    canvas_width = float(sys.argv[11])
    image_frequency = float(sys.argv[12])
    
    """
    python3 main.py num_boids sky_width initial_speed max_boid_speed num_gens proximity separation_factor
    alignment_factor cohesion_factor time_step canvas_width image_frequency
    """
    
    # generate an initial sky
    print("Generating initial sky")
    boids = []
    for _ in range(num_boids):
        theta= random.random() * math.pi * 2
        boid = Boid(OrderedPair(random.random() * sky_width, random.random() * sky_width), OrderedPair(initial_speed * math.cos(theta), initial_speed * math.sin(theta)), OrderedPair(0, 0))
        boids.append(boid)
    initial_sky = Sky(sky_width, boids, max_boid_speed, proximity, separation_factor, alignment_factor, cohesion_factor)
    
    print("Simulating")
    skies = simulate_boids(initial_sky, num_gens, time_step)
    
    print("Animating")
    surfaces = animate_system(skies, canvas_width, image_frequency)
    
    print("Rendering")
    save_video_from_surfaces(surfaces, "output/boids3.mp4", fps=10, codec = "libx264", quality = 8)
    """
    boids: 200 5000 1.0 2.0 8000 200 1.5 1.0 0.02 1.0 2000 20
    boids2: 200 5000 1.0 2.0 8000 300 3.0 1.0 0.01 1.0 2000 20
    boids3: 500 5000 1.0 2.0 8000 100 4.0 1.0 0.01 1.0 2000 20
    """

if __name__ == "__main__":
    main()

"""
Rendering helpers for animating a Universe with pygame.
"""

import math
import pygame
import imageio
import numpy as np  # for surface to numpy arrays
from datatypes import Body, OrderedPair, Universe

# Python doesn't have constants
JUPITER_MOON_MULTIPLIER = 10.0

# Drawing functions

def save_video_from_surfaces(
    surfaces: list[pygame.Surface],
    video_path: str,
    fps: int,
    codec: str,
    quality: int,
) -> None:
    """
    Save a list of pygame.Surface frames to a video file.

    Args:
        surfaces: List of pygame.Surface objects representing frames.
        video_path: Path where the video will be written.
        fps: Frames per second for the output video.
        codec: Video codec (default "libx264", requires ffmpeg).
        quality: Quality level for encoding (higher = better quality, larger file).

    Returns:
        None
    """
    writer = imageio.get_writer(video_path, fps=fps, codec=codec, quality=quality)

    for surface in surfaces:
        frame = pygame.surfarray.array3d(surface).swapaxes(0, 1)  # (H, W, 3)
        writer.append_data(frame)

    writer.close()

def pygame_surface_to_numpy(surface: pygame.Surface) -> np.ndarray:
    """
    Convert a pygame Surface to a NumPy RGB array of shape (H, W, 3).

    This is handy for exporting frames via imageio/moviepy later.
    """
    if not isinstance(surface, pygame.Surface):
        raise TypeError("surface must be a pygame.Surface")

    return pygame.surfarray.array3d(surface).swapaxes(0, 1)

def animate_system(
    time_points: list[Universe],
    canvas_width: int,
    drawing_frequency: int
) -> list[pygame.Surface]:
    """
    Render selected frames of the system into pygame surfaces.

    Frames are sampled every `drawing_frequency` simulation steps; trail history
    is updated more frequently using `TRAIL_FREQUENCY` so trails look smooth.

    Args:
        time_points: Snapshots of the Universe over time (0..N).
        canvas_width: Width/height (px) of the square canvas.
        drawing_frequency: Draw a frame when i % drawing_frequency == 0.

    Returns:
        A list of pygame.Surface objects (one per drawn frame).
    """
    if not isinstance(time_points, list):
        raise TypeError("time_points must be a list of Universe objects")
    if len(time_points) == 0:
        raise ValueError("time_points must not be empty")

    for u in time_points:
        if not isinstance(u, Universe):
            raise TypeError("all elements of time_points must be Universe objects")

    if not isinstance(canvas_width, int) or canvas_width <= 0:
        raise ValueError("canvas_width must be a positive integer")
    if not isinstance(drawing_frequency, int) or drawing_frequency <= 0:
        raise ValueError("drawing_frequency must be a positive integer")

    surfaces = []
    i = 0
    for i, u in enumerate(time_points):
        if i % drawing_frequency == 0:
            current_surface = draw_to_canvas(u, canvas_width)
            surfaces.append(current_surface)
    return surfaces

def draw_to_canvas(
    u: Universe,
    canvas_width: int,
    # trails: dict[int, list[OrderedPair]],
) -> pygame.Surface:
    """
    Draw a single Universe snapshot onto a new pygame Surface.
    """
    # --- lightweight parameter checks ---
    if not isinstance(u, Universe):
        raise TypeError("u must be a Universe")
    if not isinstance(canvas_width, int) or canvas_width <= 0:
        raise ValueError("canvas_width must be a positive integer")
    # if not isinstance(trails, dict):
    #     raise TypeError("trails must be a dict[int, list[OrderedPair]]")

    surface = pygame.Surface((canvas_width, canvas_width))
    surface.fill((255, 255, 255))
    
    for b in u.bodies:
        color = (b.red, b.green, b.blue)
        center_x = int(b.position.x/u.width * canvas_width)
        center_y = int(b.position.y/u.width * canvas_width)
        radius = b.radius/u.width * canvas_width
        print(b.name)
        if b.name in ("Io", "Ganymede", "Europa", "Callisto"):
            radius *= JUPITER_MOON_MULTIPLIER
        
        pygame.draw.circle(surface, color, (center_x, center_y), radius)
        b.position
    
    return surface

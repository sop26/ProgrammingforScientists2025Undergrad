import pygame

def draw_face() -> None:
    """
    Draws a simple cartoon face onto the given Pygame surface.
    The face consists of:
      - A large white head (circle)
      - Two black eyes (circles)
      - A small black nose (circle)
      - A red rectangular mouth
    Args:
        None
    Returns:
        None
    """
    # TODO Implement this!
    red = [255, 0, 0]
    white = [255, 255, 255]
    blue = [0, 191, 255]
    width, height = 1000, 1000
    surface = pygame.Surface((width, height))
    pygame.draw.circle(surface, red, (500, 500), 300)
    pygame.draw.circle(surface, white, (400, 400), 30)
    pygame.draw.circle(surface, white, (600, 400), 30)
    pygame.draw.rect(surface, blue, (400, 650, 200, 25))
    
    pygame.image.save(surface, "fun.png")

def main():
    print("Drawing a head.")

    # Initialize pygame but don't open window
    pygame.init()

    draw_face()

    pygame.quit()

if __name__ == "__main__":
    main()
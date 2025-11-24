import math
from datatypes import OrderedPair, Universe, QuadTree, Node, Quadrant, Star, distance, compute_force, center_of_gravity
from copy import deepcopy


def barnes_hut(
    initial_universe: Universe,
    num_gens: int,
    time: float,
    theta: float
) -> list[Universe]:
    """
    Updates the universe for a specified number of generations and returns a list of each step of the universe
    """
    universes = [initial_universe]
    
    for i in range(num_gens):
        universes.append(update_universe(universes[i], time, theta))
        
    return universes


def update_universe(current_universe: Universe, time: float, theta: float) -> Universe:
    """
    Update the stars of the universe after one time step
    """
    new_universe = copy_universe(current_universe)
    
    root = Node(Quadrant(0.0, 0.0, new_universe.width))
    quadtree = QuadTree(root)
    
    print("Insert")
    for star in new_universe.stars:
        if new_universe.in_field(star.position):
            root.insert(star)
    
    print("Update values")
    for star in new_universe.stars:
        old_accel = star.acceleration
        old_vel = star.velocity
        star.acceleration = update_acceleration(star, quadtree, theta)
        star.velocity = update_velocity(star, time, old_accel)
        star.position = update_position(star, time, old_accel, old_vel)
        
    return new_universe

def generate_quadtree(universe: Universe) -> QuadTree:
    # TODO: implement
    pass

G = 6.67408e-11  # gravitational constant (you can scale this for visualization)

# Here are some helper functions for updating star properties.
# They use the quadtree to compute gravitational forces efficiently.
# They are mostly taken from our previous n-body simulation code (note that update_acceleration() requires the quadtree).

def update_acceleration(star: Star, q:QuadTree, theta: float) -> OrderedPair:
    """
    Update the acceleration of all stars in the universe based on gravitational forces
    computed from the Barnes–Hut quadtree.

    F = ma  ⇒  a = F / m
    """
    if q.root is None or star.mass == 0.0:
        return OrderedPair(0.0, 0.0)

    # Compute the net force on star
    force = (q.root).calculate_net_force(star, theta)

    # Avoid division by zero for massless bodies
    if star.mass == 0.0:
        return OrderedPair(0.0, 0.0)
    else:
        ax = force.x / star.mass
        ay = force.y / star.mass
        return OrderedPair(ax, ay)

def update_velocity(star: Star, time: float, old_accel: OrderedPair) -> OrderedPair:
    """Update a star’s velocity using the trapezoidal integration rule."""

    # Guard against None vectors
    star.acceleration = star.acceleration or OrderedPair(0.0, 0.0)
    new_velocity = OrderedPair(0.0, 0.0)

    # Trapezoidal integration
    dvx = 0.5 * (old_accel.x + star.acceleration.x) * time
    dvy = 0.5 * (old_accel.y + star.acceleration.y) * time
    new_velocity = OrderedPair(star.velocity.x + dvx, star.velocity.y + dvy)

    return new_velocity


def update_position(star: Star, time: float, old_accel: OrderedPair, old_vel: OrderedPair) -> OrderedPair:
    """Update a star’s position using constant-acceleration motion equations."""
    new_position = OrderedPair(0.0, 0.0)

    dx = 0.5 * old_accel.x * time * time + old_vel.x * time
    dy = 0.5 * old_accel.y * time * time + old_vel.y * time
    new_position = OrderedPair(star.position.x + dx, star.position.y + dy)

    return new_position

def copy_universe(current_universe: Universe) -> Universe:
    """
    Create a fresh Universe object with independent Star copies.
    Each Star gets new position, velocity, and acceleration objects
    so that updates won't mutate the original Universe.

    Note: I use this instead of deepcopy because it is a little faster.
    """
    new_stars: list[Star] = []

    for s in current_universe.stars:
        new_star = Star(
            position=OrderedPair(s.position.x, s.position.y),
            velocity=OrderedPair(s.velocity.x, s.velocity.y),
            acceleration=OrderedPair(s.acceleration.x, s.acceleration.y),
            mass=s.mass,
            radius=s.radius,
            red=s.red,
            green=s.green,
            blue=s.blue,
        )
        new_stars.append(new_star)

    return Universe(width=current_universe.width, stars=new_stars)
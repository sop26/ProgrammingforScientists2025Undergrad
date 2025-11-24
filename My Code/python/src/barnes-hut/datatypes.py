from dataclasses import dataclass
import math
import random

G = 6.67408e-11  # gravitational constant (you can scale this for visualization)

@dataclass
class OrderedPair:
    """
    A simple 2-D point or vector with named coordinates.

    Used to represent positions, velocities, and accelerations of stars
    in the simulation. Supports access via `.x` and `.y` for readability.
    """
    x: float = 0.0
    y: float = 0.0

@dataclass
class Star:
    """
    A celestial body in the simulation.

    Each Star has a position, velocity, acceleration, mass, and radius,
    along with optional RGB color values for visualization.
    The position and motion are expressed as 2D vectors (x, y).
    """
    position: OrderedPair | None = None
    velocity: OrderedPair | None = None
    acceleration: OrderedPair | None = None
    mass: float = 0.0
    radius: float = 0.0
    red: int = 255
    green: int = 255
    blue: int = 255


@dataclass
class Universe:
    """
    A square universe of given width containing a list of stars.

    The universe defines the simulation space. Its width represents the
    side length of a square region with corners at (0, 0) and (width, width).
    """
    width: float = 0.0
    stars: list[Star] = None

    def in_field(self, p: OrderedPair) -> bool:
        """
        Check if a given point is within the bounds of the universe.
        """
        return 0 <= p.x <= self.width and 0 <= p.y <= self.width


@dataclass
class Quadrant:
    """
    A square subregion of the universe given by its lower-left corner (x, y) and width.
    """
    x: float = 0.0
    y: float = 0.0
    width: float = 0.0


@dataclass
class Node:
    """
    A node in the Barnes–Hut quadtree.

    Each node corresponds to a quadrant of space (`sector`).
    - Leaf nodes contain at most one real star.
    - Internal nodes store a “dummy” star representing the combined
      center of mass of all stars in their sub-quadrants.
    - Child quadrants are ordered [NW, NE, SW, SE].
    """
    sector: Quadrant | None = None
    star: Star | None = None
    children: list["Node"] | None = None  # [NW, NE, SW, SE]

    def is_leaf(self) -> bool:
        """
        Returns whether or not the current node is a leaf node
        """
        if self.children == None or len(self.children) == 0:
            return True
        return False

    def create_children(self) -> None:
        """
        Creates children corresponding to 4 subquadrants of the node's quadrant
        """
        new_width = self.sector.width / 2
        north_y = self.sector.y + new_width
        west_x = self.sector.x
        south_y = self.sector.y
        east_x = self.sector.x + new_width
        
        nw = Node(Quadrant(west_x, north_y, new_width), None, None)
        ne = Node(Quadrant(east_x, north_y, new_width), None, None)
        sw = Node(Quadrant(west_x, south_y, new_width), None, None)
        se = Node(Quadrant(east_x, south_y, new_width), None, None)
        
        self.children = [nw, ne, sw, se]

    def find_child(self, s: Star) -> "Node":
        """
        Finds the child whose sector would contain a specified star 
        """
        star_x = s.position.x
        star_y = s.position.y
        
        for child in self.children:
            child_x = child.sector.x
            child_y = child.sector.y
            child_width = child.sector.width
            in_x = (star_x >= child_x and star_x < child_x + child_width)
            in_y = (star_y >= child_y and star_y < child_y + child_width)
            
            if in_x and in_y:
                return child
            
        raise ValueError("Invalid coordinates - not in the current node's sector")


    def center_of_gravity(self, stars: list[Star]) -> OrderedPair:
        """
        Returns the center of gravity by computing the weighted average of the stars' positions
        """
        total_mass = 0
        weighted_x = 0
        weighted_y = 0
        
        for star in stars:
            total_mass += star.mass
            weighted_x += star.mass * star.position.x
            weighted_y += star.mass * star.position.y
            
        cg_x = weighted_x / total_mass
        cg_y = weighted_y / total_mass
        
        return OrderedPair(cg_x, cg_y)

    def insert(self, s: Star) -> None:
        """
        Inserts a star into the quadtree with the current node as the root
        """
        """
        if leaf:
            if no star - set to new star
            if yes star - create children - find best child for current star and new star
                if best child overlap, set best child to current star. insert new star in best child
                    update best child value
                set children to current and new star
                update current value

        else:
            get best child
            child.insert
            update current
        
        
        """
        if self.is_leaf():
            if self.star != None:
                self.create_children()
                node_s = self.find_child(s)
                node_old_s = self.find_child(self.star)
                self_star = self.star
                self.star = None
                if node_s == node_old_s:
                    node_s.star = self_star
                    node_s.insert(s)
                else:
                    node_old_s.star = self_star
                    node_s.star = s
                self.update_dummy_star()
            else:
                self.star = s
        else:
            node = self.find_child(s)
            node.insert(s)
            self.update_dummy_star()
            
    def update_dummy_star(self) -> Star:
        """
        Updates the internal node stars
        """
        new_pos = self.center_of_gravity(child.star for child in self.children if child.star != None) 
        new_mass = 0
        
        for child in self.children:
            if child.star != None:
                new_mass += child.star.mass
                
        self.star = Star(position=new_pos, mass=new_mass)

    def calculate_net_force(self, s: Star, theta: float) -> OrderedPair:
        """
        Computes the net force acting on one star by other stars using a heuristic
        """
        net_x = 0.0
        net_y = 0.0
        if self.star != None and self.star != s:
            dx = self.star.position.x - s.position.x
            dy = self.star.position.y - s.position.y
            d = math.sqrt((dx)**2 + (dy)**2)
            if self.is_leaf():
                f_mag = G * self.star.mass * s.mass/d**2
                return OrderedPair(f_mag * dx / d, f_mag * dy / d)
            elif d != 0:
                s_const = self.sector.width
                if s_const/d > theta:
                    for child in self.children:
                        net_force = child.calculate_net_force(s, theta)
                        net_x += net_force.x
                        net_y += net_force.y
                else:
                    f_mag = G * self.star.mass * s.mass/d**2
                    return OrderedPair(f_mag * dx / d, f_mag * dy / d)
                         
        return OrderedPair(net_x, net_y)  
@dataclass
class QuadTree:
    """
    A wrapper around the root node of a Barnes–Hut quadtree.

    Provides an interface for inserting stars, building the spatial tree,
    and calculating net gravitational forces using hierarchical aggregation.
    """
    root: Node | None = None

    def insert(self, s: Star) -> None:
        self.root.insert(s)

# To prevent circular import issues, we define these functions here.

def center_of_gravity(self, stars: list[Star]) -> OrderedPair:
        """
        Returns the center of gravity by computing the weighted average of the stars' positions
        """
        total_mass = 0
        weighted_x = 0
        weighted_y = 0
        
        for star in stars:
            total_mass += star.mass
            weighted_x += star.mass * star.position.x
            weighted_y += star.mass * star.position.y
            
        cg_x = weighted_x / total_mass
        cg_y = weighted_y / total_mass
        
        return OrderedPair(cg_x, cg_y)


def compute_force(s1: Star, s2: Star) -> OrderedPair:
    """
    Compute the gravitational force exerted by s1 on s2.
    Uses Newton's law of universal gravitation.
    𝐹 = G * (m1 * m2) / r²
    """
    d = distance(s1.position, s2.position)
    F = G * s1.mass * s2.mass / (d * d)  
    
    delta = (s1.position.x - s2.position.x, s1.position.y - s2.position.y)
    force = OrderedPair(F * (delta[0] / d), F * (delta[1] / d))
    return force


def distance(p1: OrderedPair, p2: OrderedPair) -> float:
    """
    Compute the Euclidean distance between two points.
    """
    dx, dy = (p1.x - p2.x, p1.y - p2.y)
    return math.sqrt(dx * dx + dy * dy)
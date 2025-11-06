# five fields for rectangle:
# width, height, x1, y1 (center or top left), rotation

# place class declarations between imports and def main

from dataclasses import dataclass
import copy

@dataclass
class Rectangle:
    """
    Represents a 2D rectangle with width, height, position, and rotation

    Attributes:
        width: (float)
        height: (float)
        x1: the x-coordinate of the rectangle's origin (float)
        y1: the y-coordinate of the rectangle's origin (float)
        rotation: rotation of shape in degrees (float)
    
    Class Attributes:
        description: describes some characteristic of the object (string) 
    """

    description: str = "boxy"
    width: float = 1.0
    height: float = 1.0
    rotation: float = 0.0
    x1: float = 0.0
    y1: float = 0.0

    def area(self) -> float:
        """
        Method to return the area of the rectangle
        """
        return self.width * self.height
    
    def translate(self, a: float, b: float) -> None:
        """
        Method to translate a shape a units in the x direction and b units in the y direction
        """
        self.x1 += a
        self.y1 += b
        
    def scale(self, f: float) -> None:
        """
        Dilate the shape of f.
        """
        self.width *= f
        self.height *= f
        
class Circle:
    """
    Represents a 2D circle via its center and radius.
    
    Attributes:
        x1: the x-coordinate of the center (float)
        y1: the y-coordinate of the center (float)
        radius: the center's radius (float)

    Class Attributes:
        description: describes some characteristic of the object (string) 
    """

    description: str = "round"

    x1: float = 0.0
    y1: float = 0.0
    radius: float = 1.0
   
    def area(self) -> float:
        """
        Method to return the area of the circle
        """
        return 3.14 * self.radius**2
    
    def translate(self, a: float, b: float) -> None:
        """
        Method to translate a shape a units in the x direction and b units in the y direction
        """
        self.x1 += a
        self.y1 += b
    
    def scale(self, f: float) -> None:
        """
        Dilate the shape of f.
        """
        self.radius *= f

@dataclass
class Node:
    name: str = ""
    age: float = 0.0
   
@dataclass
class Tree:
    nodes: list = None
    label: str = ""
        
def tree_trouble():
    t = Tree(nodes=[Node("A", 1), Node("B", 2)], label = "This is t.")
    print("Original t:", t)
    
    """
    sus
    s = Tree()
    s.label = t.label
    s.label = "This is s."
    s.nodes = t.nodes
    s.nodes[0].name = "Fred" #this changes t.nodes since they have the same reference
    """
    
    s = copy.deepcopy(t)
    
    print("s", s)
    print("t", t)


def main():
    print("Shapes.")
    
    tree_trouble()
    
    
    n = 5
    # Python gives variable numeric ID (not memory address)
    print("Outside function before change:", n, id(n))
    change_value(n)
    print("Outside function after change:", n, id(n))

    # all mutable things are passed by reference
    # imutable are passed by value
    # tuples
    # strings
    # ints, floats, booleans
    
    # in python, everything is an object and passed by object reference
    
    # q = a[8:10] q makes a copy of a
    
    # id() is useful if we have two objects we can check if they are actually the same literal object
    r1 = Rectangle(width = 3.0, height = 4.0, x1 = 0.0, y1 = 0.0)
    r2 = r1
    print(id(r2), id(r1))
    weirdest_thing_in_python_ever()
    
def weirdest_thing_in_python_ever():
    x = 42
    y = x
    z = 42
    # python prestores integers up until 255 - if use 42 instead of 420, "They can't be the same, RIGHT?" gets printed
    
    if id(x) == id(z):
        print("x and z have the same address")
    
    if id(x) == id(y):
        print("Same reference in memory") 
        
    y += 10   
    
    if id(x) == id(y):
        print("Still the same?") 
        
    y -= 10
    
    if id(x) == id(y):
        print("They can't be the same, RIGHT?") 
    
def change_value(x: int) -> None:
    print("Inside function before change: ", x, id(x))
    # id(x) should not be id(n) because a copy got created
    # you are passing the literal integer in by (object) reference
    # once you CHANGE it, it becomes DIFFERENT because integer is IMMUTABLE
    x += 10 # a new variable with name x gets created
    print("Inside function after change: ", x, id(x))

def basic_shape_stuff():
    r = Rectangle(width = 3.0, height = 4.0) # don't even need to get order right if we specify attributes
    c = Circle(x1 = 0.0, y1 = 0.0, radius = 4.0)
    print(r.area())
    print(c.area())
    r.translate(10.0, -5.0)
    c.translate(2.5, 3.5)
    print(r)
    print(c)
    r.scale(2.0)
    c.scale(0.4)
    print(r)
    print(c)    
    print(r.area())
    print(c.area())

def area_rectangle(r: Rectangle) -> float:
    """
    Compute the area of a given rectangle.
    """
    return r.width * r.height

def area_circle(c: Circle) -> float:
    """
    Compute the area of a circle.
    """
    return 3.0 * (c.radius ** 2)

# write perimeter_rectangle() and perimeter_circle() functions

def translate_rectangle(r: Rectangle, a: float, b:float) -> None:
    """
    Move a rectangle by a given amount in x- and y-directions.
    """
    r.x1 += a 
    r.y1 += b 

def translate_circle(c: Circle, a: float, b:float) -> None:
    """
    Move a circle by a given amount in x- and y-directions.
    """
    c.x1 += a
    c.y1 += b

if __name__ == "__main__":
    main()
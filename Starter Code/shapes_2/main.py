# five fields for rectangle:
# width, height, x1, y1 (center or top left), rotation

# place class declarations between imports and def main

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

    # Every class declaration should have a constructor to set fields
    # Also, Python calls fields "attributes"
    # We will allow the user to set attributes of an instance the second it is born
    def __init__(self, width: float=0.0, height: float=0.0, x1: float=0, y1: float=0, rotation: float=0):
        # let's protect the program from a bad user 
        if width < 0.0 or height < 0.0:
            raise ValueError("width and height must be nonnegative.")
        # we could add tests for if variables are all floats, etc.
        
        # what attributes should every Rectangle get?
        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation

    def __repr__(self) -> str:
        # let's have a nice f string to print the attributes 
        return f"Rectangle(width={self.width},height={self.height},x1={self.x1}, y1={self.y1}, rotation={self.rotation})"
    
    def area(self) -> float:
        """
        Method to return the area of the rectangle
        """
        return self.width * self.height
        
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

    def __init__(self, x1: float=0, y1: float = 0, radius: float = 0):
        if radius < 0.0:
            raise ValueError("width and height must be nonnegative.")
        self.x1 = x1
        self.y1 = y1
        self.radius = radius

    def __repr__(self) -> str:
        # let's have a nice f string to print the attributes 
        return f"Circle(x1={self.x1}, y1={self.y1}, radius={self.radius})"
    
    def area(self) -> float:
        """
        Method to return the area of the circle
        """
        return 3.14 * self.radius**2


def main():
    print("Shapes.")
    r = Rectangle(width = 3.0, height = 4.0) # don't even need to get order right if we specify attributes
    c = Circle(x1 = 0.0, y1 = 0.0, radius = 3.0)
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
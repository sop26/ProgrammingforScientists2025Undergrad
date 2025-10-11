# place class declarations between imports and def main

class Rectangle:
    """
    Represents a 2D recatngle
    
    Attributes:
        width: (float)
        height: (float)
        x1: the x coordinate of the rectangle's origin (float)
        y1: the y coordinate of the rectangle's origin (float)
        rotation: rotation of shape in degrees (float)
        
    Class Attributes:
        description: describes some characteristic of the object (string)
    """
    description: str = "boxy"
    # Every class declaration should have a constructor to set fields
    # Python calls fields "attributes"
    def __init__(self, width: float =0.0, height: float =0.0, x1: float =0.0, y1: float =0.0, rotation: float =0.0):
        # what attributes should every Rectangle get
        if width < 0.0 or height < 0.0:
            raise ValueError("width and height must be nonnegative.")
        
        self.width = width
        self.height = height
        self.x1 = x1
        self.y1 = y1
        self.rotation = rotation
        
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, x1={self.x1}, y1={self.y1}, rotation={self.rotation})"


class Circle:
    """
    Represents a 2D circle
    
    Attributes:
        x1: the x coordinate of the center (float)
        y1: the y coordinate of the center (float)
        radius: (float)
        
    Class Attributes:
        description: describes some characteristic of the object (string)
    """
    description: str= "round"
    
    def __init__(self, x1: float = 0.0, y1: float = 0.0, radius: float = 0.0):
        if radius < 0.0:
            raise ValueError("radius must be nonnegative.")
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
        
    def __repr__(self) -> str:
        return f"Circle(x1={self.x1}, y1={self.y1}, radius={self.radius})"
    

def main():
    print("Shapes.")
    my_circle = Circle(0.0, 0.0, 1.0)
    r = Rectangle(1.0, 1.0, 0.0, 0.0, 30.0)

    print(my_circle)
    print(r)
    r.width = 2.0
    r.height = 4.5
    r.x1 = -1.45
    r.y1 = 2.3
    r = Rectangle(1.0, 1.0, 0.0, 0.0, 30.0)
    print(area_circle(my_circle))
    
    print(r.description)
    #1. access it through instance
    #2. access it through class
    print(Circle.description)
    my_circle.description = "orb-like" # creates a new (local) attribute of my_circle and doesn't affect other circles
    
    # instance of a new class are passed by reference 
    
# you can't name functinos the same thing in Python (except when you can)
    
def area_rectangle(r: Rectangle) -> float:
    """
    Compute the area of a given rectangle.
    """
    return r.width * r.height

def area_circle(c: Circle) -> float:
    """
    Compute the area of a given circle.
    """
    return 3.14 * (c.radius **2)

def perimeter_rectangle(r: Rectangle) -> float:
    """
    Compute the perimeter of a given rectangle.
    """
    return 2 * r.width + 2 * r.height

def perimeter_circle(c: Circle) -> float:
    """
    Compute the area of a given circle.
    """
    return 2 * 3.14 * c.radius

def translate_rectangle(r: Rectangle, a: float, b: float) -> None:
    r.x1 += a
    r.y1 += b

def translate_circle(c: Circle, a: float, b: float) -> None:   
    c.x1 += a
    c.y1 += b
  
if __name__ == "__main__":
    main()
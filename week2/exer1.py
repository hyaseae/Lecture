"""
using copilot for making a big structure.
"""


class Vector2():
    """ simple 2 dimentional vector class, 
    including init, add, sub, eq, str.
    """
    def __init__(self, x, y):
        """initailizing the vector. x and y should be real numbers."""
        if type(x) is not int and type(x) is not float:
            print("x should be number!")
            return None
        if type(y) is not int and type(y) is not float:
            print("y should be number!")
            return None
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """adding two vectors."""
        if type(other) is not Vector2:
            print("it cannot be added!")
            return None
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """sub two vector."""
        if type(other) is not Vector2:
            print("it cannot be subtrafcted!")
            return None
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """check if two bectors are equal."""
        if type(other) is not Vector2:
            print("other is not a vector in two dimention!")
            return False  # in this case, it is false, obiously.
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """make vector form (x,y)"""
        return f"({self.x}, {self.y})"

    def __mul__(self, scalrar):
        """multipling vector with a number."""
        if type(scalrar) is not int and type(scalrar) is not float:
            print("it should be scalrar, for now.")
            # make it later I guess??
            return None
        return Vector2(self.x * scalrar, self.y * scalrar)
    
    
# main code.

v1 = Vector2(1, 2)
v2 = Vector2(3, 4)

# +
print(v1+v2)
# -
print(v1-v2)
# ==
print(v1 == v2)
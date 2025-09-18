import math
from abc import abstractmethod, ABC


class Shape3D(ABC):
    @abstractmethod
    def volume():
        pass

    @abstractmethod
    def surface_area():
        pass

    def concrete(self):
        return "shape"
    


class Cube(Shape3D):
    def __init__(self,side):
        """init's cube class"""
        super().__init__()
        self.side = side
    
    def concrete(self):
        return f"A cube with side {self.side}"
    
    def surface_area(self):
        return (self.side)**2*6
    
    def volume(self):
        return (self.side)**3
    
class Sphere(Shape3D):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    
    
    def concrete(self):
        return f"A sphere with side {self.radius}"
    
    
    def surface_area(self):
        return 4*math.pi*(self.radius)**2

    
    def volume(self):
        return (self.radius)**3 * 4 / 3 * math.pi


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        super().__init__()
        self.radius, self.height = radius, height


    def concrete(self):
        return f"A cylinder with height {self.height} and radius {self.radius}"

    def surface_area(self):
        return math.pi*(self.radius)**2*2+self.height*math.pi*self.radius

    
    def volume(self):
        return math.pi*(self.radius)**2*self.height

shapes = [Cube(2),Sphere(3), Cylinder(radius=2,height=5)]

for s in shapes:
    print(f"I'm {s.concrete()} and my volume is {s.volume()} and my surface area is {s.surface_area()}")


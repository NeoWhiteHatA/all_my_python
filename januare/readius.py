from math import pi
class Circle():
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return (self.radius * self.radius) * 2 * pi
    
        
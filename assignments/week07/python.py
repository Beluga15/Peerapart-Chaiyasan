class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width
         

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * (self.length + self.width)
         
    
rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

import math

class myCircle:
    def __init__(self, r):
        self.r = r
        

    # Method to get the area
    def get_area(self):
        return  math.pi * (self.r ** 2)
         

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * math.pi * self.r
         
    
myCircle = myCircle(10)
print(myCircle.get_area())       
print(myCircle.get_perimeter())        
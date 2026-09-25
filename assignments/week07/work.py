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
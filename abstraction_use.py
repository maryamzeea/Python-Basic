from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return f"The area of the rectangle is {self.length * self.width}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return f"The area of the circle is {math.pi * (self.radius ** 2)}"


r = Rectangle(20,20)
c= Circle(40)
print(c.area())
print(r.area())
from math import pi
class Circle :
    def __init__(self,radius,color) :
        self.radius = radius
        self.color = color
    def get_radius(self) :
        return self.radius
    def set_radius(self,change_radius = 0) :
        self.radius+=change_radius
        return self.radius
    def get_color(self) :
        return self.color
    def set_color(self,change_color) :
        self.color=change_color
        return self.color
    def get_area(self) :
        return 2*pi*self.radius**2
    def get_circumference(self) :
        return 2*pi*self.radius
    def get_info(self) -> None :
        print("\nradius =",c.get_radius())
        print("color =",c.get_color())
        print("area =",c.get_area())
        print("circumference =",c.get_circumference())

radius = int(input('radius= '))
color = input('color: ')
c = Circle(radius,color)
print("\nradius =",c.get_radius())
n = input("If you want to change circle color input 1: ")
if int(n) == 1 :
    change_color = input("color:")
    print(c.set_color(change_color))
else :
    pass
print("color =",c.get_color())
print("area =",c.get_area())
print("circumference =",c.get_circumference())
print("\ncircle info:")
c.get_info()
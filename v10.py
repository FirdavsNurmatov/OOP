class Rectangle :
    def __init__(self,height,width) :
        self.height = height
        self.width = width
    def get_height(self) :
        return self.height
    def set_height(self,change_height) :
        self.height = change_height
    def get_width(self) :
        return self.width
    def set_width(self,change_width) :
        self.width = change_width
    def get_area(self) :
        return self.height*self.width
    def get_perimeter(self) :
        return 2*(self.height+self.width)
    def get_info(self) -> None :
        print("height =",c.get_height())
        print("width =",c.get_width())
        print("area =",c.get_area())
        print("perimeter =",c.get_perimeter())

height = 4
width = 5
c = Rectangle(height,width)
print("perimeter: ",c.get_perimeter())
print("area: ",c.get_area())

print("height =",c.get_height())
change_height = 6
c.set_height(change_height)
print("set height =",c.get_height())

print("width =",c.get_width())
change_width = 10
c.set_width(change_width)
print("set widht =",c.get_width())

print("\nrectangle info:")
c.get_info()
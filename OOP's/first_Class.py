# Our first python Class
class Cuboid:

    # Constructor
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h

    # Method
    def lid_Area(self):
        return self.length * self.breadth
    
    def volume(self):
        return self.length * self.breadth * self.height
    
# Creating Object    
c1 = Cuboid(10,5,3)
print(c1.volume())

c2 = Cuboid(20,10,5)
print(c2.volume())
print(c2.lid_Area())

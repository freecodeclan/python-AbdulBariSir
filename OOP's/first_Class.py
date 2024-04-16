# Our first python Class
class Cuboid:

    # Constructor
    def __init__(self,l=1,b=1,h=1):
        self.length = l
        self.breadth = b
        self.height = h

    # Method
    def lid_Area(self):
        return self.length * self.breadth
    
    def volume(self):
        return self.length * self.breadth * self.height
    
# Creating Object    
c1 = Cuboid()
print(c1)

print()

c2 = Cuboid(10)
print(c2.lid_Area())

print()

c3 = Cuboid(10,5,5)
print(c3.volume())

# Inheritance

class Rectagle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def get_length(self):
        return self.length
    
    def set_length(self, l):
        self.length = l

    def get_breadth(self):
        return self.breadth
    
    def set_breadth(self, b):
        self.breadth = b

    def area(self):
        return self.length * self.breadth
    
    def permeter(self):
        return 2 * (self.length + self.breadth)
    
# Creating Child class which will inherit from super/parent class

class Cuboid(Rectagle):
    
    def __init__(self, l, b, h):
        self.height = h
        super().__init__(l, b)      # By using super() keyword only we can call parent class constructor 

    def get_length(self):
        return super().get_length()
    
    def set_length(self, l):
        return super().set_length(l)

    def volume(self):
        return self.length * self.breadth * self.height

r1 = Rectagle(10,5)
print(r1.get_length())
print(r1.area())


r2 = Rectagle(20,10)
print(r2.get_length())
r2.set_breadth(5)
print(r2.get_breadth())

c1 = Cuboid(10, 5, 5)
print(c1.get_length())
print(c1.area())
print(c1.volume())


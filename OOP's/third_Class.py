# Accessors and Mutators (Getters and Setters)

class Rectangle:
    
    # Constructor
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    # Using getter to read the value 
    def get_length(self):
        return self.length
    
    # Using Setter to set the new value
    def set_length(self, l):
        self.length = l

    # Method
    def area(self):
        return self.length * self.breadth
    

# Creating Object
    
r1 = Rectangle(10,5)
print(r1.get_length())

r1.set_length(20)
print('New Length:', r1.get_length())

print('Area of rectangle is:',r1.area())
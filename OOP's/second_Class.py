# Discussing about Class Variable and Class Method
class Rectangle:

    count = 0       # Class Variable

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

        Rectangle.count += 1        # Here accessing class variable inside constructor with the name of Class_Name.class_variable

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
    @classmethod
    def count_Rectangle(cls):
        print(cls.count)
    

# Now Creating Object

r1 = Rectangle(10,5)
r2 = Rectangle(15, 5)

Rectangle.count_Rectangle()     # Accessing class method with the Class_Name.class_methodName


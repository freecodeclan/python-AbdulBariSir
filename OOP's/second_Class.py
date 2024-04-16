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

    @staticmethod
    def isSquare(len, bre):
        return len==bre
    

# Now Creating Object

r1 = Rectangle(10,5)

r2 = Rectangle(15, 5)

print()

Rectangle.count_Rectangle()     # Accessing class method with the Class_Name.class_methodName

print(r1.isSquare(10,5))    # Caliing Static Method
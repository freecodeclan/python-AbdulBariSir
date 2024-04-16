# OOP's in Python
In Python object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. The main concept is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data.

The core OOP's principles are :

**1. Classes** are just the blue print of objects. Attributes are the names given to the variables that make up a class.

**2. Objects -** are class instance with a defined set of properties is called an object.

**3. Inheritance** simply means borrowing or inherit the features from existing class. The class that derives or borrow properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.

**4. Encapsulation**  means combining all the related things together and wrapping them into the single capsule or box. 

**5. Polymorphism** simply means one name and different actions.

**6. Abstraction** is hiding unnecessary details from the user and providing only those functions which are useful to user. Abstraction can be achieved with the help of encapsulation.

    class Book:
        
        def __init__(self, title, quantity, author, price):
            self.title = t
            self.quantity = t
            self.author = q
            self.price = p
    
    Note:- The __init__ special method, also known as a Constructor, is used to initialize the Book class with attributes such as title, quantity, author, and price.

    In Python, built-in classes are named in lower case, but user-defined classes are named in Camel or Snake case, with the first letter capitalized.

    The term self is the reference to the current object. When we use the term self in Python class methods, it's like saying "this object" or "the object itself."

**Class Variable -** A class variable is a variable that is shared by all instances of a class. It is declared outside of any method in the class definition. Class variables are also known as static variables.

    class Rectangle:

    count = 0       # Class Variable

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

        Rectangle.count += 1    # Accessing Class Variable
    
    @classmethod
    def count_Rectangle(cls):
        print(cls.count)

**👍Class Method -** A class method is a method that is associated with a class, rather than with any particular instance of the class. Class methods are also known as static methods.

**👍Accessors and Mutators** are commonly  referred to as **getters and setters**.  They are methods used to access and modify the values of attributes (variables) of an object, especially when those attributes are declared as private (using a single leading underscore _ convention).

    🔸Getter(Accessor) :- A getter is a method used to retrieve the value of an attribute from an object. It allows you to access the value of a private attribute without directly accessing it from outside the class. 


    🔸Setter(Mutator) :- A setter is a method used to modify the value of an attribute in an object. It allows you to change the value of a private attribute while performing certain checks or operations if needed.



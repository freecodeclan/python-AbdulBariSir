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

# Inheritance
A class's ability to inherit methods and/or characteristics from another class is known as inheritance. The subclass or child class is the class that borrows. The superclass or parent class is the class from which methods and/or attributes are inherited.

    class Rectangle:
        def __init__(self, l, b):
            self.length = l
            self.breadth = b

    class Cuboid(Rectangle):
        def __init__(self, l, b, h):
            self.heigth = h
            super().__init__(l, b)  # super() keyword is used to inherit the properties of parent class

**👍__str__** method is used to define how an object should be represented as a string. When you print an object or convert it to a string (for example, by using the str() function), Python looks for the __str__ method in the object's class.

    class Person:

        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastame = lname

        def printname(self):
            print(f'My name is {self.firstname} {self.lastame}')

        def __str__(self):
            return (f'My name is {self.firstname} {self.lastame}')

    person1 = Person('Harsh', 'Mehra')
    print(person1)

# Polmorphism
Polymorphism means one name and different actions. The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.  

Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

**👍 Duck Typing -** It is a concept that focuses on an object's behavior rather than its type. It's based on the idea that "if it looks like a duck and quacks like a duck, it must be a duck." In Python, this means that you can use any object that implements the necessary methods or attributes required by your code, without worrying about its specific type.

    def PetLover(pet):
        pet.talk()
        if hasattr(pet,'walk'):     
            pet.walk()

    class Duck:

        def talk(self):
            print('Duck is Talking')

        def walk(self):
            print('Duck is walking')

    class Dog:
        def talk(self):
            print('Dog is talking')


    dk = Duck()     # Duck object created
    PetLover(dk)    # Calling Petrover function and passing dk object of Duck() as parameter

    print()

    dg = Dog()
    PetLover(dg)

**Method Overloading -** Method Overloading is used to achieve polymorphism. Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. 

Python does not support method overloading by default. But there are different ways to achieve method overloading in Python. The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. 





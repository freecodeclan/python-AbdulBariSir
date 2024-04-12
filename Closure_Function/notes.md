# Closures
Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

In Python, we can create a function inside another function. This is known as a nested function.

    
    def greet(name):        # outer function

        def display_name(): # inner function

            print("Hi", name)
        
        display_name()  # call inner function


    greet("John")  # call outer function

    Output: Hi John

Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.

# Here closure is a factory function 

def closure(msg):
    # msg = 'Hello' 

    # Nested function
    def display():
        print('*' * 5)
        print()
        print(msg)      # Accessing msg a non local-variable inside nested function
        print()
        print('*' * 5)
    return display

d = closure('Hello World')
d()
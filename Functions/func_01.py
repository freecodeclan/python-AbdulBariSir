# Defining function to add 3 numbers

def add_3 (a, b, c):
    result = a + b + c
    return result

r = add_3(20, 30, 40)   # Positional Argument
print(r)

# Example for Positional VS Keyword Argument

def net_sal (baisc, allowance, deduction):

    net_salary = baisc + allowance - deduction
    return net_salary

net = net_sal(deduction=2000, baisc=6000, allowance=8000)   # Keyword Argument
print('The net salary is :', net)

print()

# Default Argument
def add (a, b=0, c=0):  # Here by setting value to 0 set default argument
    return a + b - c

print(add(10,20))
print(add(10, 20, 5))
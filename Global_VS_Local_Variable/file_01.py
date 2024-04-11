# Sample function 1

g = 10      # global variable

def fun(a, b):
    c = a + b       # Local Variable
    print('Local', c)
    print('Global', g)

fun(5,5)        # Calling function

print()

# Sample function 2
x = 20

def fun1():
    x = 20
    print('Local', x)

fun1()
print(f'{x}')



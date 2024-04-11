# Modifying global variable inside function using global keyword

x = 10

def fun1():
    global x        # using global keyword to modify its value inside function
    g = x + 5
    print('Now we are modifying global x ', g)

fun1()
print(x)




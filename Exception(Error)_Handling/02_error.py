# Handling erros with the help of functions

def divide (a,b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError
    


try:
    a = int(input('Enter first number: '))
    b = int(input('Enter the second number: '))

    c = divide(a,b)
    print(f'The division of {a} divided by {b}  is {c}')

except:
    print('Zero divison error')
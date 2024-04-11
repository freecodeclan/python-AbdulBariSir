# Find factorial of given number using recursion

n = int(input('Enter the value of n: '))

def fact (n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
factorial = fact(n)
print(f'The factorial of 5 is {factorial}')

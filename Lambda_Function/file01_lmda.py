# Regular function

def sum (a,b):
    c = a + b
    return c

print('Regular function', sum(10, 20))

print()

# Lammbda Expression

sub = lambda a, b : abs(a - b)

print('Lambda Expression', sub(10,20))

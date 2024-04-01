# Find the factorial of given number

n = int(input('Enter the number: '))
fact = 1

for count in range(1,n+1):
    fact *= count

print(fact)
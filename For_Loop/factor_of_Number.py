# Find the factor of Number 
n = int(input("Enter the number\n"))    #  Takig input from user

for i in range(1, n+1):
    if n % i == 0:
        print(i)




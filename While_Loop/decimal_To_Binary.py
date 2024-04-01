# Convert a decimal number to a Binary number 
n = int(input("Enter the number\n"))

bin = ''

while n > 0:
    remainder = n % 2
    n = n // 2
    bin = str(remainder) + bin

print(bin)
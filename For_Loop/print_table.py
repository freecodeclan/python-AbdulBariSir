# Prit the table of 5 using for loop

n = int(input("Enter the number for table to be printed: "))

for count in range(1,11):
    print(n, '*', count, '=', n*count)
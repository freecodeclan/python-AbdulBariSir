n = int(input("Enter the number to count the digits\n"))
count = 0
while n > 0:
    remainder = n % 10
    n = n // 10
    count += 1

print("The total number of digts: ", count)
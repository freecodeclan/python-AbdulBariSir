# Check if the number is prime or not

n = int(input("Enter the range: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("It's Prime")
else:
    print("It's not prime")

#Find the maximum number from the given numbers 

num_of_nos = int(input("Enter the number of number\n"))

count = 0

max = int(input('Enter the num'))

while count < num_of_nos - 1 :
    n = int(input("Enter the num"))
    count += 1
    if n > max:
        max = n

print('Max number is :', max)

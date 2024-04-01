#Find sum of given numbers as input
num_of_nos = int(input('Give the range of numbers\n'))
sum = 0
count = 0

while count < num_of_nos:
    n = int(input('Enter a number : '))
    sum += n
    count += 1

print('Sum is :', sum)




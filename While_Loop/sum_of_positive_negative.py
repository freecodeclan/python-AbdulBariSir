# Find the sum of positive and Negative numbers
num_of_nos = int(input("Enter the number\n"))
pst_sum = 0
ngt_sum = 0
count = 0

while count < num_of_nos:
    n = int(input("Enter the number : "))
    if n > 0:
        pst_sum += n
    else: 
        ngt_sum += n
    count += 1

print('Positive sum is: ', pst_sum)
print('Negative sum is: ', ngt_sum)

n = int(input("Enter the number\n"))
rev_num = 0

while n > 0:
    r = n % 10  # By doing mod we get remainder 
    n = n // 10
    rev_num = rev_num * 10 + r

print("The reversed number is : ", rev_num)
print(n)

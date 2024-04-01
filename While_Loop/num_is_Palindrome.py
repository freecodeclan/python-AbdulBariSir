n = int(input("Enter the number\n"))
m = n   # Storing original copy into m variable 
rev_Num = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev_Num = rev_Num * 10 + r

print('Number is palindrome') if m == rev_Num else print('Number is not palindrome')
# Check a string is palindrome 

s1 = input('Enter a String\n')

rev = s1[::-1]

print('Palindrome') if s1 == rev else print('Not Palindrome')


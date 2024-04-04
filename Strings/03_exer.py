# Check if the password ad confirm password are same

password1 = input('Enter your password\n')
password2 = input('Re-enter your password\n')

if password1 == password2:
    print('👍')
else:
    if password1.casefold() == password2.casefold():
        print('Please check for the cases')
    else:
        print('👎')


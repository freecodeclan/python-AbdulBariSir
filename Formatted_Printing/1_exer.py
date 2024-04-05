a = 22
b = 7
c = a / b

print('The division of {} and {} is {}'.format(a,b,c))

print()


# Python String .format() Method
name = input('Please enter your name: ')
age = int(input('Enter your age: '))

print('My name is {} and I am {} year old'.format(name,age))

print()

# f-strings Method -- introduced in Python 3.6
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
role = 'SWE'
company = input('Please enter your company name: ')

print(f'I am {name} and I am {age} years old. I work in {company} as {role}')
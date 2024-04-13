
try:
    a = int(input('Enter the first value: '))
    b = int(input('Enter the second value: '))
    c = a // b
    print('Try block executed')

except ZeroDivisionError as err:
    print(f'Actual Description of error: {err}')

else:
    print(f'The division of {a} and {b} is {c}')

print()

print('Outside try-except-else')

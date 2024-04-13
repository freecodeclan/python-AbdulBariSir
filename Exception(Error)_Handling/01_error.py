# Example for Exceptions/Error

# Index Error -- if user input the index out of the range than the program will show runtime error and it's on user side

list1 = [10 ,20, 30 ,40, 50]
index = int(input('Enter the valid index number: '))

print(f'The value at index {index} is ', list1[index])

''' Output :- Traceback (most recent call last):
                File "E:\Python-AbdulBari\Exception(Error)_Handling\01_error.py", line 6, in <module>
                    print(f'The value at index {index} is ', list1[index])
                                                 ~~~~~^^^^^^^
            IndexError: list index out of range '''
print()

# Value Error --- The below error will be displayed if user enter the invalid value

val = int(input('Enter the valid value: '))

print(val, type(val))

'''
Traceback (most recent call last):
  File "E:\Python-AbdulBari\Exception(Error)_Handling\01_error.py", line 18, in <module>
    val = int(input('Enter the valid value: '))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'abc

'''
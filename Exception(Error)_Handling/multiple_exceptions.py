# Here we'll be handling multiple errors with the help of multiple except blocks

l1 = [int(x) for x in input('Enter the list elements: ').split()]

try:
    index_value = int(input('Enter the index value: '))
    print(f'The value at index {index_value} is ', l1[index_value])

except (IndexError, ValueError) as msg:       # msg stands for actual description of the error and we can handle multiple types of error in one block also 
    print(msg)

'''except ValueError as msg:
    print('Enter only integer value b/w 0 to 5', msg) '''

print()

print('Terminated Successfully')

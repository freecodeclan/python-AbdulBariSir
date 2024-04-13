
list1 = [int(x) for x in input('Enter the list elements: ').split()]

try:
    index = int(input('Enter the index value: '))
    print(f'The index value at {index} is ', list1[index])
    
except:
    print('Invalid index value Entered')

print()

print('Program Terminated Gracefully')
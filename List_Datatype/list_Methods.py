# Creating List

roll_Num = [101, 103, 105, 107, 109, 111]

# Adding element into existing list using append() method
roll_Num.append(113) # While using append() method only 1 value can be added into list 

print(len(roll_Num))    # We can use len() function to see the size of list

# Adding collection of element into list using extend() function
roll_Num.extend('abc')
print(roll_Num)

# insert() Method -- By using insert method we Adds an element at the specified position
roll_Num.insert(1,201)
print(roll_Num)

print(roll_Num.count(103))

# index() Method
print(roll_Num)
x = roll_Num.index(107)
print(f'The index value of 107 is {x}')

y = roll_Num.index(101)
print(f'The index value of 101 is {y}')

print()

# pop() Method
print('The length of list before using pop() is ',len(roll_Num))

print() # Used to add space

roll_Num.pop(4)

print('The length of list after using pop() is ',len(roll_Num))

# reverse() Method
roll_Num.reverse()
print(roll_Num)
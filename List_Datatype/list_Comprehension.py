# List Comprehension

l1 = []
for x in range(10):
    l1.append(x)
    print(x, end=' ')

print()

l2 = [x for x in range(10)]
print(l2)

print()

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newList = [x for x in fruits if 'a' in x]
print(newList)

print()

data = input('Enter your names: ')
data1 = data.split()    # split() method convert string into list
print(data1)


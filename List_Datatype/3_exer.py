# Iterating or Traversing a List

name = list(('Harsh', 'Manish', 'Ram', 'Shyam', 'Mohan', 'Sohan'))

# Using for loop to Iterate 'name' list
for x in name:
    print(x, end=' ')

print() # used to create space between codes

# Now using for lopp by using range()
for i in range(len(name)):     # Here 'len' stands for length of list 
    print(name[i])

print()

# Now finally using while loop
i = 0
while i < len(name):
    print(name[i], end=' ')
    i += 1


# Creating Sets

A = {1, 2, 3, 5, 7}

B = {5, 7, 9, 10, 11}

# Union Method
C = A | B
print(f'The union of A U B is {C}')

print()

# Intersection Method
C = A.intersection(B) # we also write A & B
print(f'The intersection of A intersection B is {C}')

print()

# Difference Method
C = A - B   # we can also use A.difference(B)
print(f'The difference b/w A and B is {C}')

print()

 # Symmetric_Difference Method
C = A ^ B
print(f'The symentric_difference b/w A and B is {C}') 

print()





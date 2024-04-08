# Creating Sets

A = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

B = {1, 2, 3, 5, 7}

C = {4, 6, 8, 10}

# issubset() Method 
D = B.issubset(A)   # we can use <= operator for shorter syntax
print(D)

print()

# issuperset() Method
D = A.issuperset(B)
print(D)

print()
# isdisjoint() Method
D = A.isdisjoint(B)
print(D)
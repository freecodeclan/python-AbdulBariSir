# Checking and removing if there is any duplicate in list

l1 = [3, 5, 8, 9, 3, 4, 5, 9, 6]

l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)



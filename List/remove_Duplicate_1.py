# Remove duplicate elements from list without creating new list

l1 = [3, 5, 8, 9, 3, 4, 5, 9, 6]

i = 0
while i < len(l1):
    j = i + 1
    while j < len(l1):
        if l1[i] == l1[j]:
            l1.pop(j)  # Remove the duplicate element at index j
        else:
            j += 1  # Move to the next element if no duplicate is found
    i += 1

print(l1)



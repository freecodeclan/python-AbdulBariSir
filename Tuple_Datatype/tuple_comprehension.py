# Using tuple comprehension to print counting from 1 - 10

counting = tuple(x for x in range(1,11))
print(counting)

print()

# Another way to use tuple comprehension without using tuple() function

t1 = (*(x for x in range(1,11,2)),)
print(t1)
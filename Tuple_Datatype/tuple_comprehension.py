# Using tuple comprehension to print counting from 1 - 10

counting = tuple(x for x in range(1,11))
print(counting)

print()

# Another way to use tuple comprehension without using tuple() function

t1 = (*(x for x in range(1,11,2)),)
print(t1)

print()
# Now creating tuple for string
s1 = (*(x for x in 'WELCOME'),)
print(s1)

print()
# Now creating tuple with conditions
s2 = (*(x for x in 'WeLcoMe' if x.islower()),)
print(s2)
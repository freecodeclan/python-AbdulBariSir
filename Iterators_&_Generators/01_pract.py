# Iterators
nums = [1, 2, 3, 4]

obj = iter(nums)    # Creating iterators using inter() keyword

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj))    # This line of code will give us error 

print()

# Generators 
def nums():
    for i in range(1,6):
        yield i

obj = nums()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


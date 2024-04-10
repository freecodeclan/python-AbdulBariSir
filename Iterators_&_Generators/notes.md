# Iterators :
Python objects that iterate through iterable objects are called Iterators. It is used to iterate over objects by returning one value at a time. Iterators are created by using the **iter()** function. 
The function **next()** is used to get the subsequent value from the iterator.

    nums = [1, 2, 3, 4]

    obj = iter(nums)

    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))

# Generators :
A generator is a type of function that returns a generator object, which can return a sequence of values instead of a single result. The **def** keyword is commonly used to define generators. At least one **yield** statement is required in a generator.

    def nums():
        for i in range(1,6):
        yield i

    obj = nums()

    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
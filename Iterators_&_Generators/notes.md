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

**Note:- yield keyword** The yield keyword in Python is similar to the return keyword, but it allows us to return a sequence of values instead of just one. When we call a function that uses the yield keyword, the function returns a generator object. We can then iterate over the generator object to get the values that it yields.

**🔸 next( ) -** A built-in function used to return the next item in an iterator. 

**🔸 iter( ) -** A built-in function used to convert an iterable to an iterator. 

**🔸 Lazy Evaluation -** An evaluation strategy whereby certain objects are only produced when required. Consequently, certain developer circles also refer to lazy evaluation as “call-by-need.”
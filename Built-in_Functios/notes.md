# Built-in Functions :
**🔸 abs( ) -** The abs() function returns the absolute value of the specified number.

    x = abs(-50.5)
    
    50.5

**🔸all( ) -** The all() function returns True if all items in an iterable are true, otherwise it returns False.

    mylist = [0, 1, 1]

    x = all(mylist)

    print(x)    => The output will be False

**🔸ascii( ) -** The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc). The ascii() function will replace any non-ascii characters with escape characters:

    x = ascii("My name is Ståle")
    
    print(x)

    "'My name is St\\xe5le'"

**🔸 bin( ) -** The bin() function returns the binary version of a specified integer. The result will always start with the prefix 0b.

    x = bin(36)
    
    print(x)

    '0b10100'

**🔸 bool( ) -** The bool() function returns the boolean value of a specified object. The object will always return True, unless:

**1.** The object is empty, like [], (), {}

**2.** The object is False

**3.** The object is 0

**4.** The object is None

    x = bool(1)     |  x = bool({})

    print(x)        |   print(x)

    True            |   False

**🔸 bytearray( ) -** The bytearray() function returns a bytearray object. It can convert objects into bytearray objects, or create empty bytearray object of the specified size. 

The difference between **bytes()** and **bytearray()** is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.

    x = bytearray(5)

    print(x)

    bytearray(b'\x00\x00\x00\x00\x00')

    x.append(1)

    print(x)

    bytearray(b'\x00\x00\x00\x00\x00\x01')

**🔸 callable( ) -** The callable() function returns True if the specified object is callable, otherwise it returns False.

    def x():
        a = 5

    print(callable(x))

    'True'

**🔸 chr( ) -** The chr() function returns the character that represents the specified unicode.

    x = 100

    print(chr(x))

    'd'


**🔸 complex( ) -** The complex() function returns a complex number by specifying a real number and an imaginary number.

    Syntax - complex(real, imaginary)

    x = complex(3, 5)

    print(x)

    (3+5j)


**🔸 dict( ) -** The dict() function creates a dictionary.

    x = dict(name = 'Harsh', age = 32, car = 'Porsche')

    print(x)

    {'name': 'Harsh', 'age': 32, 'car': 'Porsche'}

**🔸 dir( ) -** The dir() function returns all properties and methods of the specified object, without the values.

This function will return all the properties and methods, even built-in properties which are default for all object.

**🔸 enumerate( ) -** The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.

    x = ['apple', 'banana', 'cherry']
    
    y = enumerate(x)

    print(tuple(y))

    ((0, 'apple'), (1, 'banana'), (2, 'cherry'))


**🔸 filter( ) -** The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

   ages = [5, 12, 17, 18, 24, 32]

    def myFunc(x):
        if x < 18:
        return False
        else:
        return True

    adults = filter(myFunc, ages)

    for x in adults:
        print(x,end = ' ') 

    18 24 32 

**🔸 format( ) -** The format() function formats a specified value into a specified format.

    x = 10

    print(format(x, 'b'))

    1010


The format you want to format the value into.

Legal values:

'<' - Left aligns the result (within the available space)

'>' - Right aligns the result (within the available space)

'^' - Center aligns the result (within the available space)

'=' - Places the sign to the left most position

'+' - Use a plus sign to indicate if the result is positive or negative

'-' - Use a minus sign for negative values only

' ' - Use a leading space for positive numbers

',' - Use a comma as a thousand separator

'_' - Use a underscore as a thousand separator

'b' - Binary format

'c' - Converts the value into the corresponding unicode character

'd' - Decimal format

'e' - Scientific format, with a lower case e

'E' - Scientific format, with an upper case E

'f' - Fix point number format

'F' - Fix point number format, upper case

'g' - General format

'G' - General format (using a upper case E for scientific notations)

'o' - Octal format

'x' - Hex format, lower case

'X' - Hex format, upper case

'n' - Number format

'%' - Percentage format
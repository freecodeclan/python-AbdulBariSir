# Dictioanry -
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Accessing Items
**1. By using square brackets[ ] -** We need to pass key inside square brackets and it will return the value of passed key.
    
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = thisdict["model"]

**2. By using get( ) Method -** We need to pass key as parameter for get( ) method and it will also return the value correspond to key.

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = thisdict.get('model')

**3. Get Keys -** The keys( ) method will return a list of all the keys in the dictionary.

    x = thisdict.keys()

**4. Get Values -** The values( ) method will return a list of all the values in the dictionary.

    x = thisdict.values()

**5. Get Items -** The items( ) method will return each item in a dictionary, as tuples in a list.

# Update Dictionary :-
The update() method will update the dictionary with the items from the given argument. If the item does not exist, the item will be added. The argument must be a dictionary, or an iterable object with key:value pairs.

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdict.update({"year": 2020})

# Adding Items in Dictionary :-
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdict["color"] = "red"
    
    print(thisdict)

# Removing Dictionary Items :-
There are several methods to remove items from a dictionary:

**1. pop( ) Method -** The pop( ) method removes the item with the specified key name:

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.pop("model")
    
    print(thisdict)

**2. popitem( ) Method -** The popitem( ) method removes the last inserted item (in versions before 3.7, a random item is removed instead):

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.popitem()
    
    print(thisdict)

**3. del keyword -** The del keyword removes the item with the specified key name:

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    del thisdict["model"]
    
    print(thisdict)

**The del keyword can also delete the dictionary completely:**

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    del thisdict
    print(thisdict) #this will cause an error because "thisdict" no longer exists.

**4. clear( ) Method -** The clear() method empties the dictionary:

    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.clear()
    
    print(thisdict)

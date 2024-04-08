# Sets :-
**Sets are used to store multiple items in single variable. A set is a collection which is unordered, unchangeable, hetrogenous and unindexed. Sets also donot allow duplicate values.**

**Note :-** Set items are unchangeable, but you can remove items and add new items.

    ==> Creating SETS

    set_1 = {'Python', 101, True, 'NodeJS', 5+2j}

    set_2 = set(('Slavia', 1500, 'Grey', False))

# Set Methods -
**1. union() -** The union() method returns a set that contains all items from the original set, and all items from the specified set(s). We can specify as many sets we want, separated by commas.

    Syntax - set.union(set1, set2...)

    Shorter Syntax - set1 | set2 | set3...

    A = {1,2,3,4}
    B = {3,4,5,6}
    C = A | B   # This stands for A union B

**2. intersection() -** The intersection() method returns a set that contains the similarity between two or more sets. As a shortcut, we can use the & operator instead, see example below.

    A = {1,2,3,4}
    B = {3,4,5,6}
    C = A & B   # This stands for A.intersection(B)

**3. difference() -** The difference() method returns a set that contains the difference between two sets. As a shortcut, we can use the - operator instead, see example below.

    A = {1,2,3,4}
    B = {3,4,5,6}
    C = A - B   # This stands for A.difference(B)

**4. symmetric_difference() -** The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets. As a shortcut, we can use the ^ operator instead, see example below.

    A = {1,2,3,4}
    B = {3,4,5,6}
    C = A ^ B   # This stands for A.symmetric_difference(B)

**5. issubset() -** The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False. As a shortcut, we can use the <= operator instead, see example below.

**6. issuperset() -** The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. As a shortcut, we can use the >= operator instead, see example below.

**7. isdisjoint() -** The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

**8. add() -** The add() method adds an element to the set. If the element already exists, the add() method does not add the element.

    Syntax - set.add(elmnt)

**9. discard() -** The discard() method removes the specified item from the set. This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not. 

    Syntax - set.discard(value)

**10. pop() -** The pop() method removes a random item from the set. This method returns the removed value.

    Syntax - set.pop()


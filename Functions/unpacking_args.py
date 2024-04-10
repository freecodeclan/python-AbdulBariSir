# Defining function

def fun2 (a,b,c,d):
    print(a,b,c,d)

list1 = [1,2,3,4]

l2 = ['Defender', 'Harsh', 33, 69.5]

t1 = ('Porsche', 'Mukul', 33, 82.5)

# fun2(list1)     # Here we'll get error 'fun2() missing 3 required positional arguments: 'b', 'c', and 'd''

fun2(list1[0],list1[1],list1[2],list1[3])   # Method_1 to call function for list

print()

fun2(*l2)   # Method_2 to call function and pass list as Actual parameters

print()

fun2(*t1)   # Passing tuple as parameter
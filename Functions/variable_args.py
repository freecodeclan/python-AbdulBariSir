# Variable Length Arguments

def fun1 (*args):       # Non-Keyword Arguments
    print(type(args), args)

fun1()
fun1(20.5,'Harsh',69,80)
fun1(1,2,3,4,5,6,7)

# keyword variable length argument
def fun2 (**kwargs):
    for x in kwargs.items():
        print(x)

fun2(carName = 'Verna', color = 'grey', engine = 1499)

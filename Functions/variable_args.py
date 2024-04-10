# Variable Length Arguments

def fun1 (*args):       # Non-Keyword Arguments
    print(type(args), args)

fun1()
fun1(20.5,'Harsh',69,80)
fun1(1,2,3,4,5,6,7)

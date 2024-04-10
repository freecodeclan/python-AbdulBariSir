# Function :-
A function is a block of code which only runs when it is called. We can pass data, known as parameters, into a function. A function can return data as a result.

Benefits of usig Function :-
    
    • Increase code Readability
    
    • Increase code Reusabilty

The syntax to declare function is :-

    def  function_name  (parameters) :

            # statements

            return expression

# Positional Argument VS Keyword Argument :
**↣ Positional Argument -** Positional arguments are passed to a function based on their position in the function call. 

    def add_3 (a, b, c):
        result = a + b + c
        return result

    r = add_3(20, 30, 40)   # Positional Argument
    print(r)

**↣ Keyword Argument -** Keyword arguments are passed to a function with a keyword (parameter name) and a value. The order in which keyword arguments are passed doesn't matter.

    def net_sal (baisc, allowance, deduction):

        net_salary = baisc + allowance - deduction
        return net_salary

    net = net_sal(deduction=2000, baisc=6000, allowance=8000)   # Keyword Argument
    print('The net salary is :', net)

**🔶 Variable Length Argument -**  Variable-length arguments refer to a feature that allows a function to accept a variable number of arguments in Python.

Two types of variable length arguments :

**🔸Non-Keyworded Arguments** (***args) -**  (*args) allows you to create functions that can take an unlimited number of arguments without needing to explicitly name each one.

    def fun1 (*args):     
        print(type(args), args)

    fun1()
    fun1(20.5,'Harsh',69,80)
    fun1(1,2,3,4,5,6,7)

Here we can pass function without any parameters, with any type of parameters and with more than one parameters.

**🔸 Keyworded Arguments** (****kwargs) -** 



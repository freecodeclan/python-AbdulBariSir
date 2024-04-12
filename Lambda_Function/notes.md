# Lambda Expression
Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as anonymous functions(**functions without name**). 

    Syntax - lambda arguments : expression

    1. lambda is a keyword in Python for defining the anonymous function.

    2. arguments are the variables that will be used to hold the values we want to pass into function expression.

    3. expression is the code you want to execute in the lambda function.

**Note -** the anonymous function does not have a return keyword. This is because the anonymous function will automatically return the result of the expression in the function once it is executed.

    # Regular Function to sum two numbers

    def sum (a,b):
        c = a + b
        return c

    print(sum(10, 20))

    30

    # Lambda Function to subtract two numbers

    sub = lambda x, y : abs(x - y)      # abs() will return absolute value 

    print(sub(10, 20))

    10

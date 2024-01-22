"""
Function are set of statements that can be executed later or can be used later

There are 67 built-in functions.

Functions are of two types:
    1. Built-in functions:
        eg: print(), type(), len(), str(), set(), list(), tuple(), dict()

    2. User Defined Functions:
        These function are defined by the User

        syntax:
            def func_name(par1, par2, ....., panN):
                //code

            func_name(arg1, arg2, ....., argN)   function calling/invoking

        Types of Arguments:
            1. default argument
            2. keyword argument
            3. positional argument  : by default functions have positional argument
            4. variable-length argument  (*y)
            5. variable-length with Keyword argument (**y)

        Return keyword (optional)
            return keyword is used to return some value from the function
            if return is not used function returns None as the value, This is called Void Function

            can return single as well as Multiple value.

        Variable Scope:
            1. Global: variables are defined outside the function or a block of code.
                       can be accessed from in any function ,etc.

            2. Local:  variables are defined inside a function or a block of code.
                       cannot be accessed outside the function or block
                       it is created when the function is called and destroyed after functions execution

    Types of User Defined Function:
        1. Lambda function:
            It is a one line function
            It is an Anonymous Function

            syntax: var_name = lambda arg: expression

            filter(): it filters iterable elements on the basis of condition
                           syntax: filter(lambda function, list)

            map():

        2. Recursion: It is a function which has a function call in its own body

"""

# lambda function
x = 5
a = lambda x: x + 5
print(a(x))

# filter():
l = [1, 2, 3, 4, 5, 6]
ol = list(filter(lambda i: i % 2 != 0, l))
el = list(filter(lambda i: i % 2 == 0, l))

print(ol, el)

# map()
sqr_l = list(map(lambda i: i * i, l))
print(l, sqr_l)

# reduce()
# sum_l = reduce(lambda x, y: x + y, l)


# Recursion:
# summation of 1 to n

n = int(input("Enter n : "))


def summation(n):
    if n == 1:
        return 1

    return n + summation(n - 1)


print(summation(n))


# Factorial Recursion:

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(n))


# return single value
def summ(a, b):
    s = a + b
    return s

print(summ(10,20))

# return multiple values

def arithmatic_operation(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a, s, m, d = arithmatic_operation(10, 5)
print(a, s, m, d)
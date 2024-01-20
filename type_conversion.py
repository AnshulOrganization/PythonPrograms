"""
Type Casting/Type Conversion is a process of converting one type of data into another.

Implicit Datatype Conversion:
    also called as coercion, occurs when datatype conversion occurs during compilation
    or runtime and is handled directly by Python.

Explicit Type Conversion:
    also known as Type Casting
    python provides us with Built-in function

    int()
    float()
    str()
"""

a_int = 1
b_float = 2.0
c_sum = a_int + b_float
print(c_sum, type(c_sum), sep="\n")


a = 10
b = float(a)
c = str(b)

print(a, b, c, type(c))
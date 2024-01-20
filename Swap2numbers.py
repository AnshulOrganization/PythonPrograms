"""
This is a program to Swap 2 Numbers with and without a Third Variable
"""

# Using temp variable

a = 10
b = 20
print(a, b)

temp = a
a = b
b = temp

print(a, b)

# Without temp variable
x = 5
y = 10
print(x, y)

(x, y) = (y, x)
print(x, y)
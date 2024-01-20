"""
This program takes the input of a number and find its last digit
"""

n = int(input("Enter n: "))

x = abs(n)
x = x % 10
print(x)
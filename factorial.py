"""
This is a program to find factorial of a number.
"""

n = int(input("Enter n: "))

f = 1
while n > 0:
    f *= n
    n -= 1

print(f)
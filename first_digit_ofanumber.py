"""
This is a Program to find the first digit of a given number
"""

n = int(input("Enter number: "))

while n > 10:
    n = n // 10

print(n)
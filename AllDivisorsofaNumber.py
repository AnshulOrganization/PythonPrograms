"""
This is a program to find all divisors of a number entered by the User.
"""

n = int(input("Enter number: "))

for i in range(1, n, 1):
    if n % i == 0:
        print(i)
"""
This program is used to print table of a number entered by the User
"""

n = int(input("Enter n: "))

for i in range(1, 11):
    print(n, " * ", i, " = ", n * i, sep="")
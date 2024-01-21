"""
This is a program to print n number of fibonacci sequence
"""

n = int(input("Enter n:"))


def fibonacci(n):
    a = 0
    b = 1
    print(a, b, sep=" ", end=" ")

    for i in range(2, n, 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


fibonacci(n)
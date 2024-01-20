"""
This is a program to print nth term of Arithmatic Progression
taking input a, n, d from User
    where,
        a = first term
        n = n number of term
        d = common difference
"""

a = int(input("Enter a: "))
d = int(input("Enter d: "))
n = int(input("Enter n: "))


def nth_term_arithmatic(x, y, z):
    return x + (z - 1) * y


print(nth_term_arithmatic(a, d, n))

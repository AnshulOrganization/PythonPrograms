"""
This is a program to find the nth term in Geometric Progression
taking input from the User
where a = first term
      r = common ratio
      n = n number of term
"""

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))


def nth_term_geometric(a, r, n):
    return a * r ** (n - 1)


print(nth_term_geometric(a, r, n))

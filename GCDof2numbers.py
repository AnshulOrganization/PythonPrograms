"""
This is a program to find Greatest Common Divisor of 2 numbers
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))

min_ab = min(a,b)
ans = 1
for i in range(1, min_ab + 1, 1):
    if (a % i == 0) & (b % i == 0):
        ans = i

print(ans)
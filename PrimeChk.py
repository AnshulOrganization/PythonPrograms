"""
This is a program to check if the number is a Prime Number
"""

n = int(input("enter number: "))

if n == 1:
    print("no")
elif n == 2 or n == 3:
    print("yes")
elif (n % 2 == 0) or (n % 3 == 0):
    print("no")
else:
    i = 5
    while i * i <= n:
        if (n % i == 0) & (n % (i + 2)):
            print("no")
        else:
            print("Yes")
        i += 6
"""
This is program to check if the number is Positive/Negative Even/Odd
"""

n = int(input("Enter n: "))

if n > 0:
    print("Positive ", end=" ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif n < 0:
    print("Negative ", end=" ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero")
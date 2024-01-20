"""
This is a program to count number of Digits entered by the User
"""

n = int(input("Enter n: "))

count = 0
while n > 0:
    n = n // 10
    count += 1

print(count)

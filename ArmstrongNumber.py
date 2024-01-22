"""
This is a program to check if a number is an Armstrong Number

153 --> 1^3 + 5^3 + 3^3 = 153
"""

n = input("Enter Number: ")
p = len(n)

num = int(n)
print(num, type(num))

ans = 0
while num > 0:
    r = num % 10
    ans += r ** p
    print(ans)
    num = int(num / 10)

print(ans, type(num))

if num == ans:
    print("Armstrong number")
else:
    print("Not an Armstrong Number")


"""
This is a program to check if the given string is a Palindrome.
"""

s = input("Enter s: ")

start = 0
end = len(s) - 1
flag = True

while start < end:
    if s[start] != s[end]:
        flag = False
        break
    else:
        start += 1
        end -= 1

if flag:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")

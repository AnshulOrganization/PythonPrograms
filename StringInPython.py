"""
String is a collection of characters
It can also be empty
It is immutable.
"""

s1 = "abcd"
s2 = 'abcd'
s3 = """Multiline
        String"""

print(s1, type(s1), s2, type(s2), s3, type(s3), sep="  ")

# Length of string
print(len(s1))
print(len(s2))
print(len(s3))

# Accessing the string characters
print(s1[0])

# slicing/substring
print(s1[-1:-len(s1)-1: -1])

# concatenation
s4 = "hello" + "hello"
print(s4)

# Asterisk *
s6 = "hello"*5
print(s6)

# membership Operators  (in/not in)
print(s4 in s6)
print(s3 in s4)

str1 = "Hi this is Anshul Kumbhare"
print(str1.capitalize())
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.swapcase())

str2 = "jfjdfj232kfsjdfk"
print(str2.isalnum())
print(str2.isalpha())
print(s6.isalpha())
print(str2.isdigit())
print(str2.islower())
print(str2.isupper())

# count() function

a = "geeks for geeks"
b = "geeks"
print(a.count(b[0:len(b)]))

# reverse()

print(a.replace("geeks", "seeks"))

# split()
print(a.split(" "))
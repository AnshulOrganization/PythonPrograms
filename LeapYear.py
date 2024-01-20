"""
This is a program that takes year as an input and checks if the year is a Leap Year
"""

year = int(input("Enter Year: "))

if (year % 4 == 0) & (year % 100 != 0):
    print("Leap year")
elif year % 400 == 0:
    print("leap year")
else:
    print("Not a Leap year")
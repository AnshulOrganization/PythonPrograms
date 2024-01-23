"""
try:
    code likely to have an error
except XXX:
    Alternative code
else:
    It will be executed if and only if there is no exception in side try block
finally:
    The main purpose of finally block is to maintain clean up code
"""
# 1
try:
    a = int(input("Enter a: "))
    b = int(input("enter b: "))

    div = a/b
    print(div)

except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Please enter valid digit")

# 2
try:
    a = int(input("Enter a: "))
    b = int(input("enter b: "))

    div = a/b
    print(div)

except Exception as e:
    print("Oops", e)

else:
    print("You are in else block")

finally:
    print("inside finally block")

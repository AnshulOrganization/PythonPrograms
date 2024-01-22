import random as r

otp = r.randrange(1000, 9999)
print(otp)

name = input("Enter name: ")
surname = input("Enter surname: ")

data = name + " : " + surname + "\n"

""" Writing creates new file and overrides if the existing file has same name """
fp = open("contact.txt", "w")
fp.write(data)
fp.close()

"""Append/insert in existing file"""
fp = open("contact.txt", "a")
fp.write(data)
fp.close()

"""Reading from file"""
fp = open("contact.txt", "r")
d = fp.read()
print(d)
fp.close()

fp = open("contact.txt", "r")
d = fp.readlines()  # returns a list
print(d)
fp.close()

"""Seaching contact in dictionary"""
src = input("Enter name: ")

fp = open("contact.txt", "r")
d = fp.readlines()

for i in d:
    l = i.split(" : ")
    if l[0] == src:
        print(i)
fp.close()

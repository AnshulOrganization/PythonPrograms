"""
OOP stands for Object-Oriented Programming
OOPs is a concept which consists of class and Object

class:
    - It is a Design or a Structure
    - It can also be defined as a template/Blueprint that describes the state and
      behavior of an object of its type.
    - It consists of Data Members and Members Function

Object:
    - Object are basic Runtime Real World Entities
    - it is an instance of class
    - Objects upon initialization are loaded in memory

    syntax:
        objectname = class_name()
        objectname.data_member
        objectname.member_function

    self is used to store copy of an object
    can have any name in place of self
"""


def add(a, b):
    add = a + b
    print(add)


class Person:
    id = 10
    name = "Anshul"
    age = 22

    def datamembers(self):
        print(self.id)
        print(self.name)
        print(self.age)

p1 = Person()
print(p1.datamembers())


class YourInfo:

    def getdata(self):
        self.name = input("Enter name: ")
        self.mob = input("Enter mob no: ")

    def show(self):
        print(self.name, self.mob, sep="\n")

c1 = YourInfo()
c2 = YourInfo()

c1.getdata()
c2.getdata()

c1.show()
print()
c2.show()
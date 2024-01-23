# Pillars of OOPs
"""
    1. Class and Object:
        Class is a design or a structure or a template
        Object is an instance of a class, It is a real world entity

    2. Encapsulation:
        the process of wrapping data members(variables) and methods
        in a single unit is called Encapsulation

        The single unit is called Class

        eg:
            class
               |
               |
        _______|___________
       |                   |
    data members         Methods
"""

# Need Of Encapsulation
"""
    1. Security
        a. Access Specifiers
             1.public
             2.private
             3.protected

"""
# 1(a1). public:
"""
    1. By default, all data members and methods inside class are public
    2. In public access, data members and methods can be accessed
        inside as well as outside the class with object.
"""

class customer:
    def getdata(self):
        self.name = input("Enter name: ")

c1 = customer()
c1.getdata()
print(c1.name)


# How to call one method inside another method

class customer:
    def getdata(self):
        self.name = input("Enter name: ")
        self.display()

    def display(self):
        print("Customer Name: ", self.name)
c1 = customer()
c1.getdata()
print(c1.name)



"""
1(a2).private:
data members and method declared private can be accessed
only inside class in method and not outside of class 
"""


# making data member private:

class customer:
    def getdata(self):
        self.__name = input("Enter name: ")

    def display(self):
        print("Customer Name: ", self.__name)

c1 = customer()
c1.getdata()
c1.display()
print(c1.name)


# making methods strongly private:

class customer:
    def getdata(self):
        self.name = input("Enter name: ")
        self.__display()

    def __display(self):
        print("Customer Name: ", self.name)

c1 = customer()
c1.getdata()
c1.__display()



class customer:
    def getdata(self):
        self.name = input("Enter name: ")
        self._display()

    def _display(self):
        print("Customer Name: ", self.name)


c1 = customer()
c1.getdata()


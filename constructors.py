"""
These are special method that is used to initialize object at the time of its creation.

syntax: __init()__
        It is automatically called when the object is created.
"""


class customer:
    def __init__(self):
        self.bank = "SBI"
        self.ifsc = "ISBN01020"
        self.add = "Online"
        print("Constructor is called :)")

    def getdata(self):
        self.cus_name = input("Enter your name: ")
        self.mob = input("Enter mob no: ")

    def display(self):
        print("Bank name: ", self.bank)
        print("IFSC: ", self.ifsc)
        print("Add: ", self.add)
        print("Cus_Name: ", self.cus_name)
        print("Mob no: ", self.mob)


c1 = customer()
c2 = customer()

c1.getdata()
c2.getdata()

c1.display()
c2.display()
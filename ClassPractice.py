"""
Class Student
"""

class student:

    def __init__(self):
        self.board = None
        self.name = None
        self.school_code = None

    def getstudata(self):
        self.name = input("name: ")
        self.school_code = int(input("School Code: "))
        self.board = input("Board : ")

    def show(self):
        print(self.name, self.school_code, self.board, sep="\n")

s1 = student()
s1.getstudata()
s1.show()
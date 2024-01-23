"""It is a special method which is used to release memory space
    allocated to the object after its use.
syntax:
     __del__():

    destructor is called or invoked automatically
    when program control reached end.
"""

class customer:
    def __init__(self):
        print("Constructor is called and object is created")

    def __del__(self):
        print("Destructor is invoked and object memory is released")

c1 = customer()
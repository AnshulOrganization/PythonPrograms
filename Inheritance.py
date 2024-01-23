# Inheritance
"""
    The process in which one class derived from another class
    to reuse the existing properties of class

    1. Single Inheritance
        parent class
            |
        child class

        Syntax:
            class A:
                //code
            class B(A):
                //code
    2. Multilevel Inheritance

           parent        A
             |           |
        Intermediate     B
             |           |
          Derived        C


    3. Multiple Inheritance

        B1 B2 B3 B4....Bn
        |__|__|___|____|
              |
              D1

        Syntax:
            class A:
                //code
            class B:
                //code
            class C(A, B):
                //code

    4. Hierarchical Inheritance
        A
     ___|___
    |       |
    B       C

     syntax:
         class A:
             //code
         class B(A):
             //code
         class C(A):
             //code:

    5. Hybrid Inheritance

            A
         ___|___
        |       |
        B       C
        |_______|
            |
            D

"""

# Single Inheritance

class A:
    def geta(self):
        self.a = int(input("Enter value for a: "))
class B(A):
    def getb(self):
        self.b = int(input("Enter value for b: "))

    def addition(self):
        self.t = self.a + self.b
        print("Addition is: ", self.t)

b1 = B()
b1.geta()
b1.getb()
b1.addition()


# Multilevel Inheritance

class A:
    def geta(self):
        self.a = int(input("Enter a: "))

class B(A):
    def getb(self):
        self.b = int(input("Enter b: "))

class C(B):
    def getc(self):
        self.c = int(input("Enter c: "))

    def addition(self):
        t = self.a + self.b + self.c
        print("Addition is: ", t)


c1 = C()
c1.geta()
c1.getb()
c1.getc()
c1.addition()


# Multiple Inheritance

class A:
    def geta(self):
        self.a = int(input("Enter a: "))

class B:
    def getb(self):
        self.b = int(input("Enter b: "))

class C(A,B):
    def getc(self):
        self.c = int(input("Enter c: "))

    def addition(self):
        t = self.a + self.b + self.c
        print("Addition is {}".format(t))


c1 = C()
c1.geta()
c1.getb()
c1.getc()
c1.addition()


# Hierarchical Inheritance

class A:
    def geta(self):
        self.a = int(input("Enter a: "))
    def getb(self):
        self.b = int(input("Enter b: "))
class B(A):
    def addition(self):
        t = self.a + self.b
        print("Addition is {}".format(t))

class C(A):
    def mul(self):
        t = self.a * self.b
        print("Multiplication is {}".format(t))

b1 = B()
b1.geta()
b1.getb()
b1.addition()

c1 = C()
c1.geta()
c1.getb()
c1.mul()


# Hybrid Inheritance

class A:
    def geta(self):
        self.a = int(input("Enter a: "))
    def getb(self):
        self.b = int(input("Enter b: "))
class B(A):
    def addition(self):
        self.t1 = self.a + self.b


class C(A):
    def mul(self):
        self.t2 = self.a * self.b


class D(B,C):
    def printVal(self):
        print("Addition is {} and Multiplication is {}".format(self.t1,self.t2))


d1 = D()
d1.geta()
d1.getb()
d1.addition()
d1.mul()
d1.printVal()



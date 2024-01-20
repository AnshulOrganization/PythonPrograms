"""
This is a calculator program with basic Arithmatic operators
"""
while(True):
    print("Select your Operation: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit ")
    move = int(input("Enter Operation number: "))

    if move == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a + b)
    elif move == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a - b)
    elif move == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a * b)
    elif move == 4:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(a / b)
    elif move == 5:
        break
    else:
        print("invalid Move")
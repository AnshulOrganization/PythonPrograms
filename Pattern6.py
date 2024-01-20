"""

         *
      *  *
   *  *  *
*  *  *  *

"""

for i in range(1, 5, 1):
    for j in range(4-i, 0, -1):
        print(" ", end="  ")

    for k in range(i, 0, -1):
        print("*", end="  ")
    print()
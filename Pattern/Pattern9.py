"""
     *
    **
   ***
  ****
 *****
 *****
  ****
   ***
    **
     *

"""

class Pattern9:
    def printPattern(self, n):
        for i in range(n):
            for x in range(n - i, 0, -1):
                print(" ", end="")
            for j in range(i + 1):
                print("*", end="")
            print()

        for i in range(n, 0, -1):
            for x in range(n - i+1, 0, -1):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()


ob = Pattern9()
rows = int(input("How Many Rows You Want in Rows"))
ob.printPattern(rows)

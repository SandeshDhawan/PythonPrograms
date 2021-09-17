"""
    *
   **
  ***
 ****
*****
"""


class Pattern3:
    def printPattern(self, n):
        for i in range(n):
            for x in range(n - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("*", end="")
            print()


row = int(input("How Many Rows You Want??"))
ob = Pattern3()
ob.printPattern(row)

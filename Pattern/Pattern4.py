"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

"""


class Pattern4:
    def printPattern(self, n):
        for i in range(n):
            for x in range(n - i):
                print(" ", end="")
            for j in range(i + 1):
                print("* ", end="")
            print()

        for i in range(n - 1, 0, -1):
            for x in range(n-i+1):
                print(" ", end="")
            for j in range(i, 0, -1):
                print("* ", end="")
            print()


rows = int(input("How Many Rows You Want??"))
ob = Pattern4()
ob.printPattern(rows)

"""
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
"""


class Pattern1:
    def printPattern(self, n):
        for i in range(n):
            for x in range(n - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("* ", end="")
            print()


ob = Pattern1()
row = int(input("How Many Rows You Want?"))
ob.printPattern(row)

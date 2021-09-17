"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

class Pattern6:
    def printPattern(self,n):
        for i in range(n,0,-1):
            for x in range(n-i):
                print(" ",end="")
            for j in range(i):
                print("* ",end="")
            print()


ob = Pattern6()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)
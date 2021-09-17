"""
     A
    A B
   A B C
  A B C D
 A B C D E
"""

class Pattern24:
    def printPattern(self, n):
        alph = 65
        for i in range(n):
            for x in range(n-i):
                print(" ",end="")
            for j in range(i + 1):
                print(chr(alph + j), end=" ")
            print()


ob = Pattern24()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

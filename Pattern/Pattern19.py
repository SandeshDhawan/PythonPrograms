"""
 1 2 3 4 5
  2 3 4 5
   3 4 5
    4 5
     5
    4 5
   3 4 5
  2 3 4 5
 1 2 3 4 5 
"""

class Pattern19:
    def printPattern(self, n):
        for i in range(1, n + 1):
            for x in range(n, n - i, -1):
                print(" ", end="")
            for j in range(i, n + 1):
                print(j, end=" ")
            print()

        for i in range(n - 1, 0, -1):
            for x in range(1, i+1):
                print(" ", end="")
            for j in range(i, n + 1):
                print(j, end=" ")
            print()


ob = Pattern19()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

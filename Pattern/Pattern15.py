"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""

class Pattern15:
    def printPattern(self, n):
        for i in range(n, 0, -1):
            for j in range(n, i - 1, -1):
                print(j, end=" ")
            print()


ob = Pattern15()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

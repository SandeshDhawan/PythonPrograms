"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7 
"""

class Pattern11:
    def printPattern(self, n):
        for i in range(1, n+1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()


ob = Pattern11()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

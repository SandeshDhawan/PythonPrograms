"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1 
"""


class Pattern16:
    def printPattern(self, n):
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()


ob = Pattern16()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

"""
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
"""

class Pattern18:
    def printPattern(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j % 2 == 0:
                    print("0 ", end="")
                else:
                    print("1 ", end="")
            print()


ob = Pattern18()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

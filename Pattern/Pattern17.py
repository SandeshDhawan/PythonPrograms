"""
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
"""


class Pattern17:
    def printPattern(self, n):
        x = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if x == 1:
                    print("1 ", end="")
                    x = 0
                else:
                    print("0 ", end="")
                    x = 1
            print()


rows = int(input("How Many Rows You Want?"))
ob = Pattern17()
ob.printPattern(rows)

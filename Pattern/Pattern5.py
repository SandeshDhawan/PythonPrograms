"""
* * * * *
* * * *
* * *
* *
* 
"""


class Pattern5:
    def printPattern(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("* ", end="")
            print()


ob = Pattern5()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

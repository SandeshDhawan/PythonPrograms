"""
*
* *
* * *
* * * *
* * * * *

"""


class Pattern2:
    def printPattern(self, n):
        for i in range(n):
            for j in range(i + 1):
                print("* ", end="")
            print()


ob = Pattern2()
row = int(input("How Many Rows You Want??"))
ob.printPattern(row)

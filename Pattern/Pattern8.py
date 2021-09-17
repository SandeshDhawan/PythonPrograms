"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""


class Pattern8:
    def printPattern(self, n):
        for i in range(n):
            for j in range(i + 1):
                print("* ", end="")
            print()

        for i in range(n - 1, 0, -1):
            for j in range(i):
                print("* ", end="")
            print()


ob = Pattern8()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

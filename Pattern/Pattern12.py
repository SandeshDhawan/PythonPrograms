"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 
"""


class Pattern12:
    def printPattern(self, n):
        x = 1
        for i in range(n):
            for j in range(i + 1):
                print(x, end=" ")
                x=x+1
            print()


ob = Pattern12()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

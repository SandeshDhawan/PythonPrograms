"""
A
B B
C C C
D D D D
E E E E E 
"""

class Pattern21:
    def printPattern(self,n):
        alph = 65
        for i in range(n):
            for j in range(i+1):
                print(chr(alph+i),end=" ")
            print()


ob = Pattern21()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)
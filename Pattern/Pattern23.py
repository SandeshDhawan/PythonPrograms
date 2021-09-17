"""
A B C D E
A B C D
A B C
A B
A
A B
A B C
A B C D
A B C D E 
"""

class Pattern23:
    def printPattern(self, n):
        alph = 65
        for i in range(n, -1, -1):
            for j in range(i):
                print(chr(alph + j), end=" ")
            if i != 0:
                print()

        for i in range(1, n ):
            for j in range(i + 1):
                print(chr(alph + j), end=" ")
            print()


ob = Pattern23()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

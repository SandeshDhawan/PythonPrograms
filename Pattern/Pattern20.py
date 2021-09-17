"""
A
A B
A B C
A B C D
A B C D E 
"""

class Pattern20:
    def printPattern(self, n):
        alph = 65
        for i in range(n):
            for j in range(i + 1):
                print(chr(alph + j), end=" ")
            print()


ob = Pattern20()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

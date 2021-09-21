"""
aA
aA bB
aA bB cC
aA bB cC dD
aA bB cC
aA bB
aA 
"""

class Pattern:
    def printPattern(self, n):
        upper_alph = 65
        lower_alph = 97
        for i in range(n):
            for j in range(i + 1):
                print(chr(lower_alph + j),end="")
                print(chr((upper_alph+j)),end=" ")
            print()

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                print(chr(lower_alph + j), end="")
                print(chr((upper_alph + j)), end=" ")
            print()



number = int(input("How Many Rows You Want"))
ob = Pattern()
ob.printPattern(number)

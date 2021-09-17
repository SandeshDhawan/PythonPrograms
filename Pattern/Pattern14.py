"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 
"""


class Pattern14:
    def printPattern(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end=" ")
            print()


ob = Pattern14()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)
"""
    1
   212
  32123
 4321234
543212345
 4321234
  32123
   212
    1
"""



class Pattern13:
    def printPattern(self, n):
        for i in range(1, n + 1):
            for x in range(n-i):
                print(" ",end="")
            for j in range(i, 0, -1):
                print(j, end="")
            for y in range(2,i+1):
                print(y,end="")
            print()

        for i in range(n-1,0,-1):
            for x in range(n,i,-1):
                print(" ",end="")
            for j in range(i,0,-1):
                print(j,end="")
            for y in range(2,i+1):
                print(y,end="")
            print()

ob = Pattern13()
rows = int(input("How Many Rows You Want??"))
ob.printPattern(rows)

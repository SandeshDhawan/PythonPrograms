"""
1 2 3 4 *
1 2 3 *  5
1 2 *  4 5
1 *  3 4 5
*  2 3 4 5
"""


class Pattrtn:
    def printPattern(self, n):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i + j == n + 1:
                    print("* ", end=" ")
                else:
                    print(j, end=" ")
            print()


ob = Pattrtn()
number = int(input("How Many Rows You Want"))
ob.printPattern(number)

class Multiplication:
    def printTable(self, n):
        for i in range(1, 11):
            print(n, "*", i, "=", n * i)


number = int(input("Which Table You Want??"))
ob = Multiplication()
ob.printTable(number)
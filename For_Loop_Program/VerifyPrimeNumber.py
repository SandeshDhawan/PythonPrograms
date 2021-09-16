class PrimeNumber:
    def printPrimeNumber(self, n):
        i = 1
        for j in range(2, n + 1):
            for i in range(2, j):
                if j % i == 0:
                    break

            if i + 1 == j:
                print(j, " is a Prime Number")
            else:
                print(j, " is not a Prime Number")


number = int(input("Enter Range for Checking Prime Numbers"))
ob = PrimeNumber()
ob.printPrimeNumber(number)
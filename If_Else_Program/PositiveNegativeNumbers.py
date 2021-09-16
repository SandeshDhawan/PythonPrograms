class PositiveNegativeNumber:
    def checkNumber(self, n):
        if n < 0:
            print(n, " is a Negative Number")
        else:
            print(n, " is a Positive Number")


number = int(input("Enter Any Number"))
ob = PositiveNegativeNumber()
ob.checkNumber(number)
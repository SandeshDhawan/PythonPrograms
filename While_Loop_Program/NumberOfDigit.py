class NumberOfDigit:
    def checkNumberOfDigit(self, n):
        cnt = 0

        while n != 0:
            cnt = cnt + 1
            n = n // 10

        print("Number of Digit is=", cnt)


number = int(input("Enter Any Number"))
ob = NumberOfDigit()
ob.checkNumberOfDigit(number)

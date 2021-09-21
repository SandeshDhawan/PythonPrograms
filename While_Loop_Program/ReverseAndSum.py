class ReverseAndSum:
    def getReverseAndSumOfNumber(self, n):
        rev = 0
        summation = 0

        while n != 0:
            p = n % 10
            rev = rev * 10 + p
            summation = summation + p
            n = n // 10

        print("Reverse is=", rev)
        print("Sum is=", summation)


number = int(input("Enter Any Number"))
ob = ReverseAndSum()
ob.getReverseAndSumOfNumber(number)

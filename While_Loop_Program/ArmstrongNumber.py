class Armstrong:
    def checkArmstrongNumber(self, n):
        rev = 0
        temp = n
        while n != 0:
            p = n % 10
            rev = rev + (p * p * p)
            n = n // 10

        print(rev)

        if rev == temp:
            print(temp, " is a Armstrong Number")
        else:
            print(temp, " is a not a Armstrong Number")


number = int(input("Enter Any Number"))
ob = Armstrong()
ob.checkArmstrongNumber(number)

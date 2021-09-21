class ConvertNumberToWords:
    def NumberConvertor(self, n):
        rev = 0
        while n != 0:
            p = n % 10
            rev = rev * 10 + p
            n = n // 10

        while rev != 0:
            p = rev % 10

            if p == 0:
                print("Zero")
            elif p == 1:
                print("One")
            elif p == 2:
                print("Two")
            elif p == 3:
                print("Three")
            elif p == 4:
                print("Four")
            elif p == 5:
                print("Five")
            elif p == 6:
                print("Six")
            elif p == 7:
                print("Seven")
            elif p == 8:
                print("Eight")
            elif p == 9:
                print("Nine")

            rev = rev // 10


number = int(input("Enter Any Number"))
ob = ConvertNumberToWords()
ob.NumberConvertor(number)

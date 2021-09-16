class EvenOddNumber:
    def checkEvenOddNumber(self, number):
        if number % 2 == 0:
            print(number, " is a Even Number")
        else:
            print(number, " is a Odd Number")


number = input("Enter Any Number")
ob = EvenOddNumber()
ob.checkEvenOddNumber(int(number))
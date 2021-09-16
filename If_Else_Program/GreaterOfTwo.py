class GreaterNumber:
    def compareNumbers(self, a, b):

        if a > b:
            print("Largest Number is=", a)
        else:
            print("Largest Number is=", b)


first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))

ob = GreaterNumber()
ob.compareNumbers(first, second)
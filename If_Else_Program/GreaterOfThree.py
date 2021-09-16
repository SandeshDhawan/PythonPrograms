class GreaterOfThree:
    def compareNumber(self, a, b, c):
        if a > b:
            d = a
        else:
            d = b

        if d > c:
            print("Largest Number is=", d)
        else:
            print("Largest Number is=", c)


first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))
third = int(input("Enter Third Number"))

ob = GreaterOfThree()
ob.compareNumber(first, second, third)
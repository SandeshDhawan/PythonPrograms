class SwapNumbers:
    def ExchangeNumber(self, first, second):
        print("Numbers Before Swapping")
        print("First Number= ", first)
        print("Second Number= ", second)

        first = first + second
        second = first - second
        first = first - second
        print("Number After Swapping")
        print("First Number= ", first)
        print("Second Number= ", second)


first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))

ob = SwapNumbers()
ob.ExchangeNumber(first, second)
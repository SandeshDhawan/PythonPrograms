class BreakNumber:
    def breakNumber(self, n):
        break_number = list()
        while n != 0:
            p = n % 10
            break_number.append(p)
            n = n // 10

        print("Splitted Number is=")
        for i in reversed(break_number):
            print(i, end=" ")


number = int(input("Enter Any Number"))
ob = BreakNumber()
ob.breakNumber(number)

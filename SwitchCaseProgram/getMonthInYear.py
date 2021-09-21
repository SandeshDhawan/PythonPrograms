class GetMonthInYear:
    def getMonth(self, n):
        if n == 1:
            print("Jan")
        elif n == 2:
            print("Feb")
        elif n == 3:
            print("March")
        elif n == 4:
            print("April")
        elif n == 5:
            print("May")
        elif n == 6:
            print("June")
        elif n == 7:
            print("July")
        elif n == 8:
            print("August")
        elif n == 9:
            print("September")
        elif n == 10:
            print("October")
        elif n == 11:
            print("November")
        elif n == 12:
            print("December")


ob = GetMonthInYear()
n = int(input("Enter Any Month Number"))
ob.getMonth(n)

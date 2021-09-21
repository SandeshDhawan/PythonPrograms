class getMonthNumberInYear:
    def getMonthNumber(self, n):
        if n == 'Jan':
            print("1")
        elif n == "Feb":
            print("2")
        elif n == "March":
            print("3")
        elif n == "April":
            print("4")
        elif n == "May":
            print("5")
        elif n == "June":
            print("6")
        elif n == "July":
            print("7")
        elif n == "August":
            print("8")
        elif n == "Sept":
            print("9")
        elif n == "Oct":
            print("10")
        elif n == "Nov":
            print("11")
        elif n == "Dec":
            print("12")


month = input("Enter Any Month")
ob = getMonthNumberInYear()
ob.getMonthNumber(month)

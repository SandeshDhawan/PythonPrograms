class ShoppingDiscount:
    def checkDiscount(self, n):

        if n >= 5000:
            print("Customer get a 50% Discount i.e ", (n * 50) / 100)
        elif 5000 > n >= 4000:
            print("Customer get a 40% Discount i.e ", (n * 40) / 100)
        elif 4000 > n >= 3000:
            print("Customer get a 30% Discount i.e ", (n * 30) / 100)
        elif 3000 > n >= 2000:
            print("Customer get a 20% Discount i.e ", (n * 20) / 100)
        elif 2000 > n >= 1000:
            print("Customer get a 10% Discount i.e ", (n * 10) / 100)
        else:
            print("No Discount")


amount = int(input("Enter Shopping Amount"))
ob = ShoppingDiscount()
ob.checkDiscount(amount)

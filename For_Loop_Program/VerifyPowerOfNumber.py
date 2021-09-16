class Power:
    def checkPowerOfNumber(self, x, n):
        res = 1
        for i in range(1, n + 1):
            res = res * x

        print(x, " Power of ", n, " is =", res)


base = int(input("Enter Base"))
power = int(input("Enter Power"))

ob = Power()
ob.checkPowerOfNumber(base, power)
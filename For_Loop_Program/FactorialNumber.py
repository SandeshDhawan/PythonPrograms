class Factorial:
    def checkFactorialNumber(self, n):
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i

        print("Factorial of Number ", n, " is =", fact)


number = int(input("Enter Any Number"))
ob = Factorial()
ob.checkFactorialNumber(number)
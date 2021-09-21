class ArithmeticOpeations:
    def performArithmeticOperations(self):
        x = True
        while x:
            print("Which Arithmetic Operation you want to perform, Select Below Operations")
            print("1-->Addition")
            print("2-->Subtraction")
            print("3-->Multiplication")
            print("4-->Division")
            n = int(input("Enter Above Option"))

            a = int(input("Enter First Number"))
            b = int(input("Enter Second Number"))

            if n == 1:
                c = a + b
                print("Addition is=", c)
                print("Do You Want to Continue??")
                y = int(input("Press 1 for yes or 0 for No"))
                if y == 1:
                    x = True
                elif y == 0:
                    x = False
            elif n == 2:
                c = a - b
                print("Subtraction is=", c)
                print("Do You Want to Continue??")
                y = int(input("Press 1 for yes or 0 for No"))
                if y == 1:
                    x = True
                elif y == 0:
                    x = False
            elif n == 3:
                c = a * b
                print("Multiplication is=", c)
                print("Do You Want to Continue??")
                y = int(input("Press 1 for yes or 0 for No"))
                if y == 1:
                    x = True
                elif y == 0:
                    x = False
            elif n == 4:
                c = a / b
                print("Division is=", c)
                print("Do You Want to Continue??")
                y = int(input("Press 1 for yes or 0 for No"))
                if y == 1:
                    x = True
                elif y == 0:
                    x = False


ob = ArithmeticOpeations()
ob.performArithmeticOperations()

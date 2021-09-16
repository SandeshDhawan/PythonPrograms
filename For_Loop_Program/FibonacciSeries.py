class Fibonacci:
    def printFibonacciNumbers(self, n):
        t1 = 0
        t2 = 1
        print(t1, end=" ")
        print(t2, end=" ")

        for i in range(n - 2):
            t3 = t1 + t2
            print(t3, end=" ")
            t1 = t2
            t2 = t3


number = int(input("How Many Numbers You Want?"))
ob = Fibonacci()
ob.printFibonacciNumbers(number)
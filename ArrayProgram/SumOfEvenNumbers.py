class SumOfEvenNumbers:
    def readArray(self):
        numbers = int(input("How Many Numbers You Want in Array"))
        array_num = list()
        for i in range(numbers):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are:")
        for i in range(numbers):
            print(array_num[i], end=" ")
        print()

        return array_num

    def sumOfEvenNumbers(self, array_values):
        evenSum = 0
        for i in range(len(array_values)):
            if array_values[i] % 2 == 0:
                evenSum = evenSum + array_values[i]

        print("Sum of Even Numbers:-", evenSum)


ob = SumOfEvenNumbers()
array_values = ob.readArray()
ob.sumOfEvenNumbers(array_values)

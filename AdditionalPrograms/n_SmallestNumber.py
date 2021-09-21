class NthSmallestNumber:
    def smallestNumber(self, array_values, n):
        for i in range(len(array_values)):
            for j in range(len(array_values) - 1):
                if array_values[j] > array_values[j + 1]:
                    temp = array_values[j]
                    array_values[j] = array_values[j + 1]
                    array_values[j + 1] = temp

        print("Sorted Array is=")
        for j in array_values:
            print(j, end=" ")
        print()

        print(n, "Smallest Number is=", array_values[n - 1])

    def enterValues(self):
        number = int(input("How Many Numbers You Want??"))
        array_numbers = list()
        for i in range(number):
            array_numbers.append(int(input("Enter Number:")))

        print("Numbers in Array are")
        for i in range(number):
            print(array_numbers[i], end=" ")
        print()
        return array_numbers


ob = NthSmallestNumber()
array_numbers = ob.enterValues()
number = int(input("Enter Which Smallest Number You Want??"))
ob.smallestNumber(array_numbers, number)

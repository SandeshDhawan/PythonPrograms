class NthLargestNumber():
    def largestNumber(self, array_values, n):
        for i in range(len(array_values)):
            for j in range(len(array_values) - 1):
                if array_values[j] > array_values[j + 1]:
                    temp = array_values[j]
                    array_values[j] = array_values[j + 1]
                    array_values[j + 1] = temp

        print("Sorted Array is=")
        for j in range(len(array_values)):
            print(array_values[j], end=" ")
        print()

        print(number, " Largest Number is= ", array_values[len(array_values) - number])

    def enter_values(self):
        number = int(input("How Many Numbers You Want??"))
        array_values = list()
        for i in range(number):
            array_values.append(int(input("Enter Number:")))

        print("Numbers in Array are")
        for i in range(number):
            print(array_values[i], end=" ")
        print()
        return array_values


ob = NthLargestNumber()
array_numbers = ob.enter_values()
number = int(input("Which Largest Number You Want??"))
ob.largestNumber(array_numbers, number)

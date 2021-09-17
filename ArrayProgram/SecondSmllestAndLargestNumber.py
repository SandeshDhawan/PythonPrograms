class SecondSmallAndLargeNumber:
    def readArray(self):
        number = int(input("How Many Numbers You Want in Array"))
        array_num = list()

        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array is=")
        for i in range(number):
            print(array_num[i], end=" ")
        print()
        return array_num

    def secondSmallestAndLargestNumber(self, array_values):
        small = array_values[0]
        large = array_values[0]
        for i in range(len(array_values)):
            if array_values[i] < small:
                small = array_values[i]

            if array_values[i] > large:
                large = array_values[i]

        maximum = small
        minimum = large
        for j in range(len(array_values)):
            if maximum < array_values[j] < large:
                maximum = array_values[j]

            if minimum > array_values[j] > small:
                minimum = array_values[j]

        print("Smallest Number:-", small)
        print("Largest Number:-", large)
        print("Second Smallest Number:-", minimum)
        print("Second Largest Number:-", maximum)


ob = SecondSmallAndLargeNumber()
array_values = ob.readArray()
ob.secondSmallestAndLargestNumber(array_values)

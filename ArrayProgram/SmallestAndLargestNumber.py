class SmallAndLargeNumber:
    def readArray(self):
        number = int(input("How Many Numbers You Want in Array"))
        array_num = list()
        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are")
        for i in range(number):
            print(array_num[i], end=" ")
        print()
        return array_num

    def smallAndLargeNumber(self, array_values):
        small = array_values[0]
        large = array_values[0]
        for i in range(len(array_values)):
            if array_values[i] < small:
                small = array_values[i]

            if array_values[i] > large:
                large = array_values[i]

        print("Smallest Number is=", small)
        print("Largest Number is=", large)


ob = SmallAndLargeNumber()
array_values = ob.readArray()
ob.smallAndLargeNumber(array_values)

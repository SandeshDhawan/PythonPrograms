class Sorting:
    def readArray(self):
        number = int(input("How Many Numbers You Want in Array"))
        array_num = list()

        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are")
        for i in range(len(array_num)):
            print(array_num[i], end=" ")
        print()
        return array_num

    def sorting(self, array_values):
        for i in range(len(array_values)):
            for j in range(len(array_values) - 1):
                if array_values[j] > array_values[j + 1]:
                    temp = array_values[j]
                    array_values[j] = array_values[j + 1]
                    array_values[j + 1] = temp

        print("Sorted Array is=")
        for i in range(len(array_values)):
            print(array_values[i], end=" ")


ob = Sorting()
array_values = ob.readArray()
ob.sorting(array_values)

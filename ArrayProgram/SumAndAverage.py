class SumAndAverage:
    def redadArray(self):
        number = int(input("How Many Numbers You Want in Array"))
        array_num = list()
        print("Enter Numbers in Array")
        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are:-")
        for i in range(number):
            print(array_num[i], end=" ")
        print()
        return array_num

    def sumandaverage(self, array_values):
        summation = 0
        for i in range(len(array_values)):
            summation = summation + array_values[i]

        print("Sum is=", summation)
        print("Average is=", summation/len(array_values))


ob = SumAndAverage()
array_values = ob.redadArray()
ob.sumandaverage(array_values)
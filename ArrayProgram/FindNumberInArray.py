class FindNumber:
    def readArray(self):
        number = int(input("How Many Numbers You Want in Array"))
        array_num = list()
        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are:")
        for i in range(number):
            print(array_num[i], end=" ")
        print()

        return array_num

    def findNumber(self, array_values, numbertosearch):
        cnt = 0
        for i in range(len(array_values)):
            if array_values[i] == numbertosearch:
                break
            else:
                cnt = cnt + 1

        if cnt == len(array_values):
            print(numbertosearch, " is not present in array")
        else:
            print(numbertosearch, " is present in array at", cnt+1, "position")


ob = FindNumber()
findNumber = int(input("Which Number You Want to Search in Array"))
array_values = ob.readArray()
ob.findNumber(array_values, findNumber)

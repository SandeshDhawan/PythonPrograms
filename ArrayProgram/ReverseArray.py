class Reverse:
    def printReverseArray(self, array_num):
        # print(array_num[::-1])

        # for i in reversed(range(len(array_num))):
        #     print(array_num[i],end=" ")
        # print()

        for i in range(len(array_num)-1,-1,-1):
            print(array_num[i],end=" ")
        print()

    def readArray(self, n):
        array_num = list()
        for i in range(n):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are:-")
        for i in range(n):
            print(array_num[i], end=" ")
        print()
        return array_num


numbers = int(input("How Many Numbers You Want in Array"))
ob = Reverse()
array_values = ob.readArray(numbers)
print("Reverse Array is=")
ob.printReverseArray(array_values)
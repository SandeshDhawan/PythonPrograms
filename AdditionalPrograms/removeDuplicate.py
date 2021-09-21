class RemoveDuplicate:

    def removeDuplicate(self, array_num):
        unique_num = set()
        for i in range(len(array_num)):
            unique_num.add(array_num[i])

        print("Array after removing duplicate number")
        for num in unique_num:
            print(num, end=" ")

    def enterValues(self):
        number = int(input("How Many Number You Want??"))
        array_num = list()
        for i in range(number):
            array_num.append(int(input("Enter Num:")))

        print("Numbers in Array are:-")
        for i in range(number):
            print(array_num[i], end=" ")
        print()
        return array_num


ob = RemoveDuplicate()
array_num = ob.enterValues()
ob.removeDuplicate(array_num)

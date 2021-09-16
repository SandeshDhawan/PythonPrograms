class EvenNumbers:
    def readArray(self, n):
        array_num = list()
        for i in range(n):
            array_num.append(input("Enter Num:"))

        print("Numbers in Array are:-")
        for i in range(n):
            print(array_num[i], end=" ")
        print()
        return array_num

    def evenNumbers(self, array_num):
        for i in range(len(array_num)):
            if int(array_num[i]) % 2 == 0:
                print(array_num[i], end=" ")


number = int(input("How Many Numbers You Want in Array"))
ob = EvenNumbers()
array_values = ob.readArray(number)
print("Even Numbers in Array are")
ob.evenNumbers(array_values)
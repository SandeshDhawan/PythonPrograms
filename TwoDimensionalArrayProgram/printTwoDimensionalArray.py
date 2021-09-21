class TwoDimensionArray:
    def getDetailsAndPrintArray(self, dim):
        rows, cols = (dim, dim)
        arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(int(input("Enter Num:")))
            arr.append(col)

        print(dim," Dimensional Array is=")
        for i in range(rows):
            for j in range(cols):
                print(arr[i][j], end=" ")
            print()


dimension = int(input("Which Dimensional Array You Want??"))
ob = TwoDimensionArray()
ob.getDetailsAndPrintArray(dimension)

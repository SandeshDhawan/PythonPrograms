class SumOfColumns:
    def readAndPrintArray(self, dim):
        rows, cols = (dim, dim)
        arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(int(input("Enter Number")))
            arr.append(col)

        print(dim, " Dimensional Array is=")
        for i in range(rows):
            for j in range(cols):
                print(arr[i][j], end=" ")
            print()
        return arr

    def sumOfColumns(self, dim, arr):
        print("Sum Of Columns is=")
        for i in range(dim):
            summation = 0
            for j in range(dim):
                summation = summation + arr[i][j]
                print(arr[i][j], end=" ")
            print("=", summation)


dimension = int(input("Which Dimension Array You Want??"))
ob = SumOfColumns()
array_values = ob.readAndPrintArray(dimension)
ob.sumOfColumns(dimension, array_values)

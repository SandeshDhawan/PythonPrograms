class SumOfDiagonal:
    def readAndPrintArray(self, dim):
        rows, cols = (dim, dim)
        arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(int(input("Enter Number:")))
            arr.append(col)

        print(dim, " Array is=")
        for i in range(rows):
            for j in range(cols):
                print(arr[i][j], end=" ")
            print()
        return arr

    def sumOfDiagonal(self, dim, arr):
        summation = 0
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    summation = summation + arr[i][j]

        print("Sum of Diagonal Number is=", summation)

    def sumOfSecondDiagonal(self, dim, arr):
        summation = 0
        for i in range(dim):
            for j in range(dim):
                if i + j == dim - 1:
                    summation = summation + arr[i][j]

        print("Sum Of Second Diagonal Number is=", summation)


dimension = int(input("Which Dimensional Array You Want??"))
ob = SumOfDiagonal()
array_values = ob.readAndPrintArray(dimension)
ob.sumOfDiagonal(dimension, array_values)
ob.sumOfSecondDiagonal(dimension, array_values)

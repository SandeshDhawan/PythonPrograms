class SumOfTriangularNumber:
    def readAndPrintArray(self, dim):
        rows, cols = (dim, dim)
        arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(int(input("Enter Number")))
            arr.append(col)

        print(dim, " Array is=")
        for i in range(rows):
            for j in range(cols):
                print(arr[i][j], end=" ")
            print()
        return arr

    def sumOfUpperTraingularNumber(self, dim, arr):
        summation = 0
        for i in range(dim - 1):
            for j in range(i + 1, dim):
                summation = summation + arr[i][j]

        print("Sum of Upper Triangular Number is=", summation)

    def sumOfLowerTraingularNumber(self, dim, arr):
        summation = 0
        for i in range(1, dim):
            for j in range(i):
                summation = summation + arr[i][j]
        print("Sum Of Lower Triangular Number is=", summation)

    def sumOfSecondUpperTriangularNumber(self, dim, arr):
        summation = 0
        for i in range(dim - 1):
            for j in range(dim - i - 1):
                summation = summation + arr[i][j]
        print("Sum of Second Upper Triangular Number is=", summation)

    def sumOfSecondLowerTringularNumber(self, dim, arr):
        summation = 0
        for i in range(1, dim):
            for j in range(dim - i, dim):
                summation = summation + arr[i][j]

        print("Sum of Second Lower Triangular Number is=", summation)


dimension = int(input("Which Dimensional Number You Want??"))
ob = SumOfTriangularNumber()
array_values = ob.readAndPrintArray(dimension)
ob.sumOfUpperTraingularNumber(dimension, array_values)
ob.sumOfLowerTraingularNumber(dimension, array_values)
ob.sumOfSecondUpperTriangularNumber(dimension, array_values)
ob.sumOfSecondLowerTringularNumber(dimension, array_values)

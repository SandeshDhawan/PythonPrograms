class TransporseMatrix:
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

    def transporseMatrx(self, dim, arr):
        transporsearr = []
        for i in range(dim):
            col = []
            for j in range(dim):
                col.append(arr[j][i])
            transporsearr.append(col)

        print("Transpose Matrix is=")
        for i in range(dim):
            for j in range(dim):
                print(transporsearr[i][j], end=" ")
            print()


dimension = int(input("Which Dimensional Array You Want??"))
ob = TransporseMatrix()
array_values = ob.readAndPrintArray(dimension)
ob.transporseMatrx(dimension, array_values)

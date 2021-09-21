class NumberCombination:
    def numberscomb(self):
        cnt = 0
        for i in range(1, 5):
            for j in range(1, 5):
                for k in range(1, 5):
                    if i != j and j != k and i != k:
                        print(i,j,k)
                        cnt=cnt+1

        print("Number count is=",cnt)


ob = NumberCombination()
ob.numberscomb()

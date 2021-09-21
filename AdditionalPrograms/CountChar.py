class countcharacter:
    def countChar(self, str):
        unique_chr = set()
        for i in range(len(str)):
            unique_chr.add(str[i])

        for char_value in unique_chr:
            cnt = 0
            for j in range(len(str)):
                if char_value == str[j]:
                    cnt = cnt + 1

            print(char_value, "-->", cnt)


str = input("Enter Any String")
ob = countcharacter()
ob.countChar(str)

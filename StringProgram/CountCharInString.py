class CountCharInStrings:
    def CountChar(self, str):
        letter = 0
        num = 0
        space = 0
        other = 0
        for i in range(len(str)):
            if str[i].isalpha():
                letter = letter + 1
            elif str[i].isdigit():
                num = num + 1
            elif str[i].isspace():
                space = space + 1
            else:
                other = other + 1

        print("Character is=", letter)
        print("Number is=", num)
        print("Space is=", space)
        print("Other Character is", other)


str = input("Enter Any String")
ob = CountCharInStrings()
ob.CountChar(str)

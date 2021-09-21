class RemoveCharacter:
    def removeCharacter(self, str, remove_chr):
        new_str = ""
        for i in range(len(str)):
            if str[i] != remove_chr:
                new_str = new_str + str[i]

        print("String After Removing Character is=", new_str)


str = input("Enter Any String")
rem_char = input("Which Character You Want to perform")
ob = RemoveCharacter()
ob.removeCharacter(str, rem_char)

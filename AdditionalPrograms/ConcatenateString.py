class Concatination:
    def concatinateTwoString(self, str1, str2):
        for value in str2:
            str1 = str1 + value

        print("Concatenated String is=", str1)


ob = Concatination()
str1 = input("Enter First String")
str2 = input("Enter Second String")
ob.concatinateTwoString(str1, str2)

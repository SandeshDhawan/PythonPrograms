class Palindrome:
    def checlPalindromeString(self, str):
        rev = ""
        for i in range(len(str) - 1, -1, -1):
            rev = rev + str[i]

        print("Reverse String", rev)

        if rev == str:
            print("String is Palindrome")
        else:
            print("String is not Palindrome")


str = input("Enter Any String")
ob = Palindrome()
ob.checlPalindromeString(str)

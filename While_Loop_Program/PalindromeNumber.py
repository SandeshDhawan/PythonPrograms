class Palindrome:
    def checkPalindromeNumber(self, n):
        rev = 0
        temp = n
        while n != 0:
            p = n % 10
            rev = rev * 10 + p
            n = n // 10

        print("Reverse is=", rev)
        if rev == temp:
            print(temp, " is a Palindrome Number")
        else:
            print(temp, " is not a Palindrome Number")


number = int(input("Enter Any Number"))
ob = Palindrome()
ob.checkPalindromeNumber(number)

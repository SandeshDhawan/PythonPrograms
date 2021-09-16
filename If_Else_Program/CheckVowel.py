class Vowel:
    def CheckVowel(self, str):
        str = str.lower()

        if str[0] == 'a' or str[0] == 'e' or str[0] == 'i' or str[0] == 'o' or str[0] == 'u':
            print(str, " is a Vowel")
        else:
            print(str, " is a Consonant")


str = input("Enter Any String")
ob = Vowel()
ob.CheckVowel(str)
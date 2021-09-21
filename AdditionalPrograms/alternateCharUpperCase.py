class UpperCase:
    def alternateChatUpperCase(self, str):
        new_str = ""
        cnt = 0
        for i in range(len(str)):
            if cnt == 0:
                new_str = new_str + str[i].upper()
                cnt = 1
            elif cnt == 1:
                new_str = new_str + str[i].lower()
                cnt = 0

        print("Updates String is=:-",new_str)


ob = UpperCase()
str = input("Enter Any String")
ob.alternateChatUpperCase(str)

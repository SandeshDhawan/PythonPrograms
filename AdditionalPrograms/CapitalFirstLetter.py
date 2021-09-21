class CapitalLetter:
    def capsFirstLetter(self, str):
        splitted_str = str.split(" ")
        new_str = ""
        for i in range(len(splitted_str)):
            new_str = new_str + splitted_str[i][0].upper()
            for j in range(1, len(splitted_str[i])):
                new_str = new_str + splitted_str[i][j]
            new_str = new_str + " "

        print("String with capital letter:-", new_str)


str = input("Enter Any String")
ob = CapitalLetter()
ob.capsFirstLetter(str)

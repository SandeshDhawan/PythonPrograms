"""
input = I Am Going To Office
Output = Office To Going Am I

input = I Am Going To Office
output = eciffO oT gnioG MA I
"""


class ReverseString:
    def reverseString(self, str):
        splitted_str = str.split(" ")

        for i in range(len(splitted_str) - 1, -1, -1):
            print(splitted_str[i], end=" ")
        print()

        for i in range(len(str) - 1, -1, -1):
                print(str[i], end="")



ob = ReverseString()
str = input("Enter Any String")
ob.reverseString(str)

"""
input = Sandesh Sunil Dhawan
output = nawahD linuS hsednaS
"""


class ReverseString:
    def reverse(self, str):

        splitted_str = str.split(" ")

        for i in range(len(splitted_str) - 1, -1, -1):
            for j in range(len(splitted_str[i]) - 1, -1, -1):
                print(splitted_str[i][j], end="")
            print(end=" ")


str = input("Enter Any String")
ob = ReverseString()
ob.reverse(str)

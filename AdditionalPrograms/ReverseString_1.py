"""
input = Sandesh Sunil Dhawan
output = Dhawan Sunil Sandesh 
"""


class ReverseString:
    def reverse(self,str):
        splitted_str = str.split(" ")
        for i in range(len(splitted_str)-1,-1,-1):
            print(splitted_str[i],end=" ")


str = input("Enter Any String")
ob = ReverseString()
ob.reverse(str)
class NumberOccurance:
    def countNumberOccurance(self, number_values):
        unique_numbers = set()
        for i in range(len(number_values)):
            unique_numbers.add(number_values[i])

        for number in unique_numbers:
            cnt = 0
            for j in number_values:
                if number == j:
                    cnt = cnt + 1
            print(number, " is coming ", cnt, " times")

    def enterNumberInLits(self):
        number_list = list()
        number = int(input("How Many Numbers You Want"))
        for i in range(number):
            number_list.append(int(input("Enter Num:")))
        return number_list


ob = NumberOccurance()
number_list = ob.enterNumberInLits()
ob.countNumberOccurance(number_list)

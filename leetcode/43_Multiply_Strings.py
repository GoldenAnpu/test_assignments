class Solution:
    def converter(self, string: str) -> int:
        new_list = []
        summa = 0
        dict_numbers = dict(enumerate(range(0, 10)))
        for number in string:
            for digit in dict_numbers.keys():
                if number == str(digit):
                    new_list.append(dict_numbers[digit])
                    break
        levels = len(new_list) - 1
        while new_list:
            summa += new_list.pop(0) * (10 ** levels)
            levels -= 1
        return summa

    def multiply(self, num1: str, num2: str) -> str:
        result = self.converter(num1) * self.converter(num2)
        return str(result)
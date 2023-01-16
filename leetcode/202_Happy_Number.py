class Solution:
    def is_happy(self, n: int) -> bool:
        summa = 0
        loop_check = []
        while True:
            for letter in str(n):
                letter = int(letter) ** 2
                summa += letter
            if summa == 1:
                answer = True
                break
            if summa in loop_check:
                answer = False
                break
            loop_check.append(summa)
            n = summa
            summa = 0
        return answer

class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        result = list(map(int, str(num)))
        return result

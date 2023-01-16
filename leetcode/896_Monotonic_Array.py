class Solution:

    # less memory usage solution
    def is_monotonic(self, nums: list[int]) -> bool:
        if 1 <= len(nums) <= 10 ** 5:
            i = 0
            j = 1
            min_num = -10 ** 5
            max_num = 10 ** 5
            b = False
            while min_num <= nums[i] <= max_num:
                if len(nums) == 1:
                    return True
                while True:
                    if nums[i] - nums[j] >= 0:
                        i += 1
                        j += 1
                        if j > len(nums) - 1:
                            b = True
                            return b
                    else:
                        i = 0
                        j = 1
                        break
                while True:
                    if nums[i] - nums[j] <= 0:
                        i += 1
                        j += 1
                        if j > len(nums) - 1:
                            b = True
                            return b
                    else:
                        break
                return b
            else:
                return False
        else:
            return False

    # fast solution
    def is_monotonic_fast(self, nums: list[int]) -> bool:
        def cmp(a, b):
            return (a > b) - (a < b)

        return not {cmp(i, j) for i, j in zip(nums, nums[1:])} >= {1, -1}
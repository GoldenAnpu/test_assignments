# 28. Find the Index of the First Occurrence in a String
class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        if 1 <= len(haystack) | len(needle) <= 10 ** 4:
            return haystack.lower().find(needle.lower())
        elif len(haystack) < len(needle):
            return -1


# 896. Monotonic Array
class Solution896:

    # less memory usage solution
    def isMonotonic(self, nums: list[int]) -> bool:
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
    def isMonotonic_fast(self, nums: list[int]) -> bool:
        def cmp(a, b):
            return (a > b) - (a < b)

        return not {cmp(i, j) for i, j in zip(nums, nums[1:])} >= {1, -1}


# 459. Repeated Substring Pattern
class Solution459:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for index in range(1, len(s)):
            no_of_occurrences = len(s) // index
            if s[0:index] * no_of_occurrences == s:
                return True
        return False


# 658. Find K Closest Elements
class Solution658:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        res_arr = arr[0:k]
        for i in range(k, len(arr)):
            if res_arr[0] == arr[i]:
                continue
            if abs(res_arr[0] - x) > abs(arr[i] - x):
                res_arr.pop(0)
                res_arr.append(arr[i])
            else:
                break
        return res_arr


# 66. Plus One
class Solution66:
    def plus_one(self, digits: list[int]) -> list[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        result = list(map(int, str(num)))
        return result


# 739. Daily Temperatures
class Solution739:
    def daily_temperatures_slow(self, temperatures: list[int]) -> list[int]:
        index_i = 0
        days_list = []
        for i in temperatures:
            index_j = index_i + 1
            append = 0
            for j in temperatures[index_j:]:
                if j > i:
                    delta = index_j - index_i
                    days_list.append(delta)
                    append += 1
                    break
                else:
                    index_j += 1
            if append == 0:
                days_list.append(0)
            index_i += 1
        return days_list

    def daily_temperatures_stack(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                val, index = stack.pop()
                ans[index] = i - index

            stack.append((t, i))
            ans.append(0)
        return ans

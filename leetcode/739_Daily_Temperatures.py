class Solution:
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
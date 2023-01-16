class Solution:
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

class Solution:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        result = []
        while True:
            try:
                [result.append(n) for n in matrix.pop(0)]
                [result.append(matrix[n].pop(-1)) for n in range(len(matrix) - 1)]
                last = matrix.pop(-1)
                last.reverse()
                [result.append(n) for n in last]
                [result.append(matrix[n].pop(0)) for n in range(len(matrix) - 1, 0, -1)]
            except:
                break
        return result
class Solution1:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False
        i = 0
        j = n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] < target:
                    break
        return False


class Solution3:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False

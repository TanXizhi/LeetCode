class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n-1, -1, -1):
                temp = matrix[j].pop(0)
                matrix[i].append(temp)
        return matrix

# 暴力解法，超出时间限制
class Solution1:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0

        maxSide = 0
        for i in range(m):
            for j in range(n):
                # 遇到一个1作为正方形的左上角
                if matrix[i][j] == '1':
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentSide = min(m - i, n - j)
                    for k in range(1, currentSide):
                        flag = True
                        # 查看对角（右下角），如果为0直接跳出循环
                        if matrix[i + k][j + k] == '0':
                            break
                        # 如果为1遍历所在的行和列，如果有0则跳出循环
                        for q in range(k):
                            if matrix[i + k][j + q] == '0' or matrix[i + q][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare


# 动态规划
class Solution2:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0]*n for _ in range(m)]
        maxSide = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i]
                                       [j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

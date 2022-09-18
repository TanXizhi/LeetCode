class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        x = len(grid[0])
        y = len(grid)
        dp = [[0]*x for _ in range(y)]
        dp[0][0] = grid[0][0]
        for i in range(1, y):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, x):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, y):
            for j in range(1, x):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[y-1][x-1]

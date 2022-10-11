class Solution1:
    def maxProfit(self, prices: list[int]) ->int:
        maxProf = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] >= prices[i-1]:
                maxProf += prices[i]-prices[i-1]
        return maxProf
        

class Solution2:
    def maxProfit(self, prices: list[int]) ->int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = 0  #第0天不持有
        dp[0][1] = -prices[0]  #第0天持有

        for i in range(1, n):
            #第i天不持有 由 第i-1天不持有然后不操作 和 第i-1天持有然后卖出 两种情况的最大值转移过来
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            #第i天持有 由 第i-1天持有然后不操作 和 第i-1天不持有然后买入 两种情况的最大值转移过来
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0]


# 将Solution2状态压缩，dp[i] 只和 dp[i - 1] 有关，去掉一维
class Solution3:
    def maxProfit(self, prices: list[int]) ->int:
        n = len(prices)
        sell = 0
        buy = -prices[0]

        for i in range(1, n):
            sell = max(sell , buy + prices[i])
            buy = max(buy, sell - prices[i])
            
        return sell


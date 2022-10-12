class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # 五个状态: 0. 没有操作 1.第一次买入 2.第一次卖出 3.第二次买入 4.第二次卖出
        dp = [[0]*5 for _ in range(n)]
        # 初始化状态，即第一天的状态
        dp[0][0] = 0  # 第一天没有操作
        dp[0][1] = -prices[0]  # 第一天第一次买入
        dp[0][2] = 0  # 第一天第一次卖出
        dp[0][3] = -prices[0]  # 第一天第二次买入
        dp[0][4] = 0  # 第一天第二次卖出

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            # 第一次买入
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            # 第一次卖出 由前一次卖出不操作和前一次买入再卖出 两种情况的最大值转移过来
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            # 第二次买入 由前一次买入不操作和前一次卖出再买入 两种情况的最大值转移过来
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            # 第二次卖出 由前一次卖出不操作和前一次买入再卖出 两种情况的最大值转移过来
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[n-1][4]


# 空间优化，将Solution1状态压缩，dp[i] 只和 dp[i - 1] 有关，去掉一维
class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [0]*5  # 五个状态: 0. 没有操作 1.第一次买入 2.第一次卖出 3.第二次买入 4.第二次卖出
        # 初始化状态，即第一天的状态
        dp[0] = 0  # 第一天没有操作
        dp[1] = -prices[0]  # 第一天第一次买入
        dp[2] = 0  # 第一天第一次卖出
        dp[3] = -prices[0]  # 第一天第二次买入
        dp[4] = 0  # 第一天第二次卖出

        for i in range(1, n):
            # 第一次买入
            dp[1] = max(dp[1], dp[0] - prices[i])
            # 第一次卖出 由前一次卖出不操作和前一次买入再卖出 两种情况的最大值转移过来
            dp[2] = max(dp[2], dp[1] + prices[i])
            # 第二次买入 由前一次买入不操作和前一次卖出再买入 两种情况的最大值转移过来
            dp[3] = max(dp[3], dp[2] - prices[i])
            # 第二次卖出 由前一次卖出不操作和前一次买入再卖出 两种情况的最大值转移过来
            dp[4] = max(dp[4], dp[3] + prices[i])

        return dp[4]


# 将Solution2语意化
class Solution3:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


class Solution4:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp1 = [0]*n
        dp2 = [0]*n
        minval = prices[0]
        maxval = prices[-1]

        for i in range(1, n):
            dp1[i] = max(dp1[i-1], prices[i]-minval)  #从前往后遍历，表示第1天到第i天之间的最大利润（通过是否在第i天卖出确认）；
            minval = min(prices[i], minval)

        for i in range(n-2, -1, -1):
            dp2[i] = max(dp2[i+1], maxval - prices[i])  #从后往前遍历，表示第i天到最后一天之间的最大利润（通过是否在第i天买进确认）；
            maxval = max(prices[i], maxval)

        dp = [dp1[i]+dp2[i] for i in range(n)]   #正好表示从第1天到最后一天经过两次交易的最大利润，我们的目标是找到令总利润最大的i。
        return max(dp)

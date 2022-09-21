# 动态规划
class Solution1:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # 当没有屋子时
        if n == 0:
            return 0
        # 当只有一间屋子时
        if n == 1:
            return nums[0]
        # 创建一个size为n的dp数组用来存储当前房子数量时能偷窃到的最大金额
        dp = [0]*n
        # 初始化...dp[0]用来存储到第一个房间时能偷窃盗到的最大金额，dp[1]用来存储到第二个房间时能偷窃盗到的最大金额
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # dp[i]用来存储到第i个房间时能偷窃盗到的最大金额, 方法是比较偷窃（前i-1间房的最高金额）和偷窃（前i-2间房的最高金额+第i间房的总金额）
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]


# 滚动数组，相较于动态规划优化了空间
class Solution2:
    def rob(self, nums: list[int]) -> int:
        pre = 0
        cur = 0
        # 每次循环，计算“偷到当前房子为止的最大金额”
        for num in nums:
            # 循环开始时，cur 表示 dp[k-1]，pre 表示 dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            pre, cur = cur, max(num+pre, cur)
            # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
        return cur

# 贪心算法
class Solution1:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        curDis = 0  # 当前覆盖的最远距离下标
        nextDis = 0  # 下一步覆盖的最远距离下标
        step = 0  # 记录步数
        """
        当移动下标指向len(nums) - 2时：
        如果移动下标等于当前覆盖最大距离下标， 需要再走一步（即step++），因为最后一步一定是可以到的终点。（题目假设总是可以到达数组的最后一个位置）
        如果移动下标不等于当前覆盖最大距离下标，说明当前覆盖最远距离就可以直接达到终点了，不需要再走一步。
        """
        for i in range(n - 1):  # 注意这里是小于n-1，这是关键所在
            if i <= curDis:  # 如果当前位置能到达，更新下一步覆盖的最远距离下标
                nextDis = max(nextDis, nums[i] + i)
                if i == curDis:  # 移动下标只要遇到当前覆盖最远距离的下标，直接步数加一，更新下一步可达的最大区域
                    curDis = nextDis
                    step += 1
        return step


# 动态规划
class Solution2:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0]*n  #dp数组用于存储跳到每个位置的最小步数
        dp[0] = 0   #初始化第一个位置，即所需最小步数为0
        for i in range(1, n):   #先将每个位置取一个较大的步数值
            dp[i] = n + 1

        for i in range(n):  #遍历数组，更新每个位置的最小步数
            for j in range(1, nums[i] + 1): #每次更新的是i位置能到达的所有位置的步数，即i往后nums[i]的位置
                if i + j >= n:    #当遍历到大于数组长度时跳出遍历，获得最后一个位置更新后的最小步数
                    return dp[n - 1]
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]

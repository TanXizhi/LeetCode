#动态规划
class Solution1:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1]*n  # 使用数组dp保存每步子问题的最优解。dp[i]代表含第i个元素的最长上升子序列的长度。
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]: #向前遍历找出比i元素小的元素j，令dp[i] 为 max（dp[i],dp[j]+1)
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


#二分查找
class Solution2:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        temp = [nums[0]]
        for num in nums[1:]: #遍历nums列表
            if num > temp[-1]: #当num大于temp列表中最后一位时直接将num加到temp列表后面
                temp.append(num)
                continue
            left, right = 0, len(temp)  #否则，通过二分查找方法找到num应该放置的位置，用它覆盖掉比它大的元素中最小的那个
            while left < right:
                mid = left + (right-left)//2
                if temp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            temp[right] = num

        return len(temp)
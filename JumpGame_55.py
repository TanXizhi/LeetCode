#贪心
class Solution1:
    def canJump(self, nums:list[int]) -> bool:
        n = len(nums)
        maxDis = 0   #初始化当前可达的最大位置
        for i in range(0, n-1):
            if i <= maxDis:  #如果当前位置能到达，更新最远能到达的位置
                maxDis = max(maxDis, nums[i]+i) 
        return maxDis >= n-1  #判断最远能到位置是否大于最后一位数的下标


#假定能跳到最后一个位置，看是否能反推到数组第一位数
class Solution2:
    def canJump(self, nums:list[int]) -> bool:
        n = len(nums)
        cur = n-1    #从最后一个位置出发
        for i in range(n-2, -1, -1):  #倒着遍历数组
            if cur <= nums[i] + i:   #更新cur位置
                cur = i
        return cur == 0   #看cur位置是否能到数组第一位
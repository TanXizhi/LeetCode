class Solution1:
    def singleNumber(self, nums: list[int]) ->int:
        nums.sort() #先排序
        l = len(nums)
        for i in range(0,l,2):  #从i=0开始两两比较，判断相邻两位是否相等，相等则继续循环
            if i == l-1:    #到最后一位都不匹配的话则返回nums[i]
                return nums[i]
            if nums[i] != nums[i+1]: #相邻两位不相等则返回nums[i]
                return nums[i]

class Solution2:
    def singleNumber(self, nums: list[int]) ->int:
        # 任何数与0异或等于任何数
        # n与n异或等于0
        # 异或满足交换律和结合律：a^b^a = b^(a^a) = b^0 = b
        ans = nums[0]
        l = len(nums)
        for i in range(1,l):   #只出现一次的数字可通过异或操作循环遍历列表筛出
            ans = ans^nums[i]
        return ans

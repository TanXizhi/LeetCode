# 标记
class Solution1:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        由于我们只在意[1, N]中的数，因此我们可以先对数组进行遍历，
        如果1不再数组，直接返回1，然后把不在[1, N]范围内的数修改1。
        这样一来，数组中的所有数就都是正数了，因此我们就可以将「标记」表示为「负号」。
        """
        n = len(nums)
        if 1 not in nums:
            return 1
        for i in range(n): #我们将数组中所有小于等于0和大于数组长度的数修改为1
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):  # 遍历数组中的每一个数x，将x的绝对值所对应位置的值标记为负的，标记过的位置对应的值说明在数组中，未标记过的位置对应的值说明不在数组中
            a = abs(nums[i]) - 1
            nums[a] = -abs(nums[a])
        for i in range(n): #遍历数组，遇到的第一个为正的位置，说明就是未标记过的，即位置对应的值为第一个缺失的正数
            if nums[i] > 0:
                return i + 1
        return n + 1  #这种情况是数组中的位置全都被标记了，那么第一个缺失的正数即为n+1


#置换
class Solution2:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


#临时数组temp
class Solution3:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        temp = [0] * n
        for i in range(n): 
            if 1 <= nums[i] <= n :
                temp[nums[i]-1] = nums[i]
        
        for i in range(n):
            if temp[i] != i + 1:
                return i + 1
        return n + 1


#从1开始遍历到2**31，第一个不在数组中的即为解
class Solution4:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        for i in range(1, 2**31):
            if i not in nums:
                return i
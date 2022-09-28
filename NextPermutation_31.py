class Solution1:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, n):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        return nums
        nums.sort()
        return nums


class Solution2:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1.先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
        2.再找出另一个最大索引 l 满足 nums[l] > nums[k]；
        3.交换 nums[l] 和 nums[k]；
        4.最后翻转 nums[k+1:]。

        """
        # 定义一个将nums中[i,j]区间的元素原地倒排的函数
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        # 从右至左找第一个相邻升序对
        n = len(nums)
        firstIndex = -1
        for i in range(n-1, -1, -1):
            if nums[i] > nums[i-1]:
                firstIndex = i-1
                break
        # 如果没有找到升序对，则数组是降序的，即本身是最大的，所以反转数组，使之成为最小的排列
        if firstIndex == -1:
            reverse(nums, 0, n-1)
            return nums
        # 从右至左找第一个大于nums[firstIndex]的大数
        secondIndex = -1
        for j in range(n-1, firstIndex, -1):
            if nums[j] > nums[firstIndex]:
                secondIndex = j
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex+1, n-1)
        return nums
        

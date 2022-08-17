class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1

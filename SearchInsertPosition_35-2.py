class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if target <= nums[i]:
                return i
        return n

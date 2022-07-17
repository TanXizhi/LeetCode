class Solution:
    def twoSum(self, nums: list[int], target:int)->list[int]:
        dict = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[num] = i
        return[]

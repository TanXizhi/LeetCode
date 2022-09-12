import collections
import random

#Sorted Order
class Solution1:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
#Hash Map
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

#Random
class Solution3:
    def majorityElement(self, nums: list[int]) -> int:
        maj = len(nums)//2
        while True:
            num = random.choice(nums)
            if nums.count(num) > maj:
                return num

#Boyer-Moore
class Solution4:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

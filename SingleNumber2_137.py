# 排序后遍历
class Solution1:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(0,n,3):
            if i == n - 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]

# 哈希表
import collections
class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        ans = [num for num, cont in count.items() if cont == 1][0]
        return ans


# 位运算
class Solution3:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
   
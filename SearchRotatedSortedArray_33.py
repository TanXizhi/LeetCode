# 有排序或者部分排序可考虑用二分查找
class Solution1:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:  # mid左侧是有序的
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # nums[mid]<nums[0]的情况，即mid右侧是有序的
                if nums[mid] < target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

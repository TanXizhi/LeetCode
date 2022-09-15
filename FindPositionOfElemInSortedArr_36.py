class Solution1:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        #二分查找，寻找target的左边界
        def leftPosition(nums: list[int], target: int):
            left = 0
            right = n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    right = mid
                else:
                    right = mid -1
            if nums[left] == target:
                return left
            else:
                return -1
        #二分查找，寻找target的右边界
        def rightPosition(nums: list[int], target: int):
            left = 0
            right = n - 1
            while left < right:
                #找右边界的target位置，mid要向上取整
                mid = (left + right + 1) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    left = mid
                else:
                    right = mid -1
            return left

        left = leftPosition(nums, target)
        if left == -1:
            return [-1,-1]
        
        right = rightPosition(nums, target)
        return [left, right]


class Solution2:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = -1
        right = -1
        n = len(nums)
        if n == 0:
            return [-1,-1]
        for i in range(n):
            if nums[i] == target:
                left = i
                break
        for j in range(n-1,-1,-1):
            if nums[j] == target:
                right = j
                break
        return [left, right]
        
    
            


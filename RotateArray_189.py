#额外数组
class Solution1:
    def rotate(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp =[0] * n
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = temp[i]
        return nums


#数组翻转
class Solution2:
    def rotate(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(0, n-1) #先翻转整个数组
        reverse(0, k-1) #再翻转前k个子串
        reverse(k, n-1) #最后翻转k到末尾的子串
        return nums
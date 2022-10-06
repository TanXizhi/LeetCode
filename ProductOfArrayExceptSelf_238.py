class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        ans = [0]*n

        #前缀之积
        left[0] = 1
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        #后缀之积
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        #前缀*后缀之积
        for i in range(n):
            ans[i] = left[i]*right[i]

        return ans


class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0]*n

        #用ans先存储前缀之积
        ans[0] = 1
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        #直接生成结果，而后求取后缀之积
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i]*right
            right *= nums[i]

        return ans
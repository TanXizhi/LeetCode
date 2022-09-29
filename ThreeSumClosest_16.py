#双指针
class Solution1:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        re_min = float('inf') #设置一个初始化差值
        n = len(nums)
        nums.sort() #先排序，再遍历

        for i in range(n): #双指针
            left = i + 1  
            right = n - 1
            if i >= 1 and nums[i] == nums[i-1]: #去重
                continue
            while left < right:  #指针跳出循环条件
                total = nums[i] + nums[left] + nums[right]
                x = target - total   #当前三数的差值
                if abs(x) < re_min:  #更新差值
                    re_min = abs(x)
                    ans = total
                if x == 0:  #如果等于target直接返回
                    return target
                elif x > 0:  #小于target左指针右移
                    left += 1
                else:              #大于target右指针左移
                    right -= 1
        return ans

#暴力解法
class Solution2:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort() #先排序，再遍历
        ans = nums[0] + nums[1] + nums[2] #设置第一组三数之和，也是最小和
        if target <= ans:
            return ans

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    total = nums[i] + nums[j] +nums[k]
                    if abs(target - total) <= abs(target - ans):
                        ans = total
        return ans


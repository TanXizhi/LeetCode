class Solution1:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        if not nums or n < 4:
            return []
        for i in range(n-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return ans


class Solution2:
    def fourSum(self, nums: list[int], target: int):
        d = {}
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                d.setdefault(nums[i]+nums[j], []).append((i, j))
        ans = set()
        for i in range(n-1):
            for j in range(i+1, n):
                for a, b in d.get(target - nums[i] - nums[j], []):
                    temp = {a, b, i, j}
                    if len(temp) == 4:
                        ans.add(tuple(sorted(nums[i] for i in temp)))
        return list(ans)

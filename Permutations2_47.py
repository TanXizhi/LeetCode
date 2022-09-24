import itertools

class Solution1:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(nums, size, depth, path, used):
            if depth == size:
                # 变量path所指向的列表在深度优先遍历的过程中只有一份，深度优先遍历完成以后回到了根结点成为空列表，所以在变成空列表前应该先拷贝一份
                ans.append(path.copy())
                return
            for i in range(size):
                # used[i]是用来判断nums[i]有没有被用过
                if not used[i]:
                    #去重, 剪枝条件：i > 0 是为了保证 nums[i - 1] 有意义
                    #used[i - 1] 是因为 nums[i - 1] 在深度优先遍历的过程中刚刚被撤销选择
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, size, depth+1, path, used)
                    used[i] = False
                    path.pop()

        #排序（升序或者降序都可以），排序是剪枝的前提            
        nums.sort()
        size = len(nums)
        used = [False for _ in range(size)]
        backtrack(nums, size, 0, [], used)
        return ans




class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(nums, temp):
            if not nums:
                #去重
                if temp not in ans:
                    ans.append(temp)
                    return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], temp + [nums[i]])
        backtrack(nums, [])
        return ans


class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        #先set是为了去重
        return list(set(itertools.permutations(nums)))
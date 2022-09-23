class Solution1:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(nums, size, depth, path, used):
            if depth == size:
                # 变量path所指向的列表在深度优先遍历的过程中只有一份，深度优先遍历完成以后回到了根结点成为空列表，所以在变成空列表前应该先拷贝一份
                ans.append(path[:])
                return
            for i in range(size):
                # used[i]是用来判断nums[i]有没有被用过
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums, size, depth+1, path, used)
                    used[i] = False
                    path.pop()

        size = len(nums)
        used = [False for _ in range(size)]
        backtrack(nums, size, 0, [], used)
        return ans




class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(nums, temp):
            if not nums:
                ans.append(temp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], temp + [nums[i]])
        backtrack(nums, [])
        return ans

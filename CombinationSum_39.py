# 回溯+剪枝
class Solution1:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates, begin, size, path, res, target):
            # 由于进入更深层的时候，小于0的部分被剪枝，因此递归终止条件值只判断等于0的情况
            if target == 0:
                res.append(path)
                return
            for index in range(begin, size):
                diff = target - candidates[index]
                # 这里剪枝，前提是候选数组已经有序，
                if diff < 0:
                    break
                dfs(candidates, index, size, path +[candidates[index]], res, diff)

        size = len(candidates)
        if size == 0:
            return []
        # 排序是剪枝的前提
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


# 动态规划
class Solution2:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 初始化一个数组dict，键是1~target，值初始化为空列表
        dict = {}
        for i in range(1, target+1):
            dict[i] = []

        for i in range(1, target+1):
            for j in candidates:
                if j == i:
                    dict[i].append([j])
                elif i > j:
                    for k in dict[i-j]:
                        x = k[:]
                        x.append(j)
                        x.sort()  # 升序，便于后续去重
                        if x not in dict[i]:
                            dict[i].append(x)

        return dict[target]

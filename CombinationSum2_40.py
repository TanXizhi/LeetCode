# 回溯+剪枝
class Solution1:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(candidates, begin, size, path, res, target):
            # 由于进入更深层的时候，小于0的部分被剪枝，因此递归终止条件值只判断等于0的情况
            if target == 0:
                res.append(path)
                return
            for index in range(begin, size):
                diff = target - candidates[index]
                # 大剪枝，前提是候选数组已经有序，
                if diff < 0:
                    break
                # 小剪枝，对于相同candidates的去重
                if index > begin and candidates[index] == candidates[index-1]:
                    continue
                dfs(candidates, index + 1, size, path + [candidates[index]], res, diff)

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
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        size = len(candidates)
        if size == 0:
            return []
        res = []
        # 从小到大排序，方便剪枝
        candidates.sort()

        def dfs(begin, path, remain):
            # 剩余为0，说明已经找到，将该路径添加到res
            if remain == 0:
                res.append(path[:])
                return
            for i in range(begin, size):
                #候选数大于剩下的目标，剪枝（大剪枝）
                if candidates[i] > remain:
                    break
                #如果当前候选数和本循环中已经使用过的候选数相同，则跳过
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                # 若候选数小于等于remain且不与之前数重合，路径中添加该候选数
                path.append(candidates[i])
                # 在余下候选数中寻找所有可能路径
                dfs(i+1, path, remain-candidates[i])
                # 将当前候选数从path中剔除（当前候选数的所有可能已经推演完毕并赋予res），
                # 继续到下一个候选数进行循环
                path.pop()
        
        dfs(0, [], target)
        return res

                


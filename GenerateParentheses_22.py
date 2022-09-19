'''
动态规划：
dp[i]表示i组括号的所有有效组合
dp[i] = "(dp[p]的所有有效组合)+【dp[q]的组合】"，其中 1 + p + q = i , p从0遍历到i-1, q则相应从i-1到0
'''

class Solution1:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n+1)]    # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]                     # 初始化dp[0]
        for i in range(1, n+1):          # 计算dp[i], 即i组括号时的括号组合
            for p in range(i):           # 遍历p
                l = dp[p]                # 得到dp[p]的所有有效组合
                r = dp[i-p-1]            # 得到dp[q]的所有有效组合
                for x in l:
                    for y in r:
                        dp[i].append("({0}){1}".format(x, y))
        return dp[n]


"""
回溯算法：
当前左右括号都大于0个可以使用的时候，才产生分支；
产生左分支的时候，只看当前是否还有左括号可以使用；
产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
在左边和右边剩余的括号数都等于0的时候结算。
"""

class Solution2:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        cur_str = ''

        def backtrack(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                ans.append(cur_str)
                return
            if left > right:      # 剪枝（左括号可以使用的个数严格大于右括号可以使用的个数，才剪枝)
                return
            if left > 0:
                backtrack(cur_str+'(', left-1, right)
            if right > 0:
                backtrack(cur_str+')', left, right-1)
        backtrack(cur_str, n, n)
        return ans

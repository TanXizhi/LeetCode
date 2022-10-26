# 动态规划dp
class Solution1:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        # 初始化dp=[False,⋯,False]，长度为n+1。n为字符串长度。dp[i]表示s的前i位是否可以用wordDict中的单词表示。
        dp = [False]*(n + 1)
        dp[0] = True  # 初始化dp[0]=True，空字符可以被表示

        for i in range(0, n):  # 遍历字符串的所有子串，遍历开始索引i，遍历区间 [0,n)
            for j in range(i + 1, n + 1):  # 遍历结束索引j，遍历区间 [i+1,n+1)
                if dp[i] == True and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]  # 返回 dp[n]


# 缓存回溯dfs
class Solution2:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        import functools  # 缓存机制,可以直接将函数或类方法的结果缓存住，后续调用则直接返回缓存的结果

        @functools.lru_cache(None)
        def dfs(s: str):
            if not s:  # 若s长度为0，则返回True，表示wordDict中的单词分割完
                return True
            res = False  # 初试化当前字符串是否可以被分割res=False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = dfs(s[i:]) or res
            return res
        return dfs(s)

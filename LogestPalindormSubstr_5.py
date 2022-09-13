class Solution:
    def longestPalindrome(self, s: str) -> str:
        n =len(s)
        if n < 2:
            return s
        
        maxLen = 1
        begin = 0
        #dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False]*n for _ in range(n)]
        #初始化：所有长度为 1 的子串都是回文串
        for i in range(n):
            dp[i][i] = True
        #由于dp[i][j]参考它左下方的值，因此应左下角先填，即先升序填列再升序填行
        for j in range (1, n):
            for i in range (0, j):
                #头尾字符不相等子串不是回文
                if s[i] != s[j]:
                    dp[i][j] = False
                #头尾字符相等有两种情况
                else:
                    #一种是边界情况 j-1-（i+1）< 1时即字符串长度为2或3时子串必须为回文
                    if j-i < 3:
                        dp[i][j] = True
                    #另一种情况参考左下角子串的值
                    else:
                        dp[i][j] = dp[i+1][j-1]
                #dp[i][j]==true成立就表示s[i...j]为回文，此时记录回文长度和起始位置
                if dp[i][j] and j-i+1 > maxLen:
                    maxLen = j-i+1
                    begin = i

        return s[begin:begin+maxLen]
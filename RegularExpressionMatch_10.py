class Solution1:
    def isMatch(self, s:str, p:str) ->bool:
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)] # 初始化
        dp[0][0] = True # 空字符串匹配

        for j in range(1, n+1): # 初始化p与空串的匹配
            if p[j-1] == '*':  # 开头都加了一位，则p中当前字符下表都要-1，s也是一样的
                dp[0][j] = dp[0][j-2] 
            else:
                False

        for i in range(1, m+1):  # 开始填表
            for j in range(1, n+1):
                if p[j-1] in {s[j-1], '.'}:  # p当前字符能匹配的情况下看它左上角位置的值
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':  # p当前字符为*时
                    if dp[i][j-2]:   # *匹配0次，看它倒着数2位的位置上的值，如果值为True则当前位置为True
                        dp[i][j] = True
                    elif p[j-2] in {s[j-1], '.'}: # *匹配一次或者多次，看它倒着数一位的字符是否为s[j-1]或'.'，如果是则当前位置的值取决于它上一行对应列的值
                        dp[i][j] = dp[i-1][j]
        return dp[m][n]
        
        
import re
class Solution2:
    def isMatch(self, s:str, p:str) ->bool:
        return True if re.compile(p).fullmatch(s) else False

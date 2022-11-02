#标记法 + 栈
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        stack = [] #栈用来存储'('
        mark = [1]*n #标记
        for i in range(n):  #遍历s，如果有成对的()则标记为0, 无法匹配的的标记为1
            if s[i] == '(':
                stack.append(i)
            else:        
                if len(stack) != 0:
                    mark[i] = 0
                    mark[stack.pop()] = 0
        
        length = 0
        res = 0
        for i in range(n): #遍历mark数组，找到最长连续的0的长度即为最长有效括号长度
            if mark[i]:
                length = 0
                continue
            length += 1
            res = max(res, length)
        return res


        
#动态规划dp数组
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp=[0]*n
        for i in range(n):
            if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2] 
        return max(dp)


#栈
class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1] #栈用来存储'('的下标，初始化值为-1，即「最后一个没有被匹配的右括号的下标」
        length = 0
        res = 0
        for i in range(n):  #遍历s，如果为左括号，将其下表放入栈
            if s[i] == '(':
                stack.append(i)
            else:         #如果为右括号，将栈中最后一位元素弹出与之匹配
                stack.pop()
                if len(stack) == 0:  #如果栈为空了，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
                    stack.append(i)
                else:    #如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」
                    length = i - stack[-1]
                    res = max(res, length)
        return res


#正向逆向结合
class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        left = right = 0
        res = 0

        #正向遍历
        for i in range(n):
            if s[i] == "(":
                left += 1
            else: 
                right += 1
            if right == left: #当左右括号相等则计算有效括号的长度
                res = max(res, right*2)
            elif right > left: #正向遍历，左括号恒大于右括号才能继续计数下去，如果右括号大于左括号那么需重置然后重新计数
                right = left = 0

        
        #逆向遍历
        right = left = 0 #重置
        for i in range(n-1, -1, -1):
            if s[i] == "(":
                left += 1
            else: 
                right += 1
            if right == left: #当左右括号相等则计算有效括号的长度
                res = max(res, right*2)
            elif left > right :  #逆向遍历，右括号恒大于左括号才能继续计数下去，如果左括号大于右括号那么需重置然后重新计数
                right = left = 0

        return res
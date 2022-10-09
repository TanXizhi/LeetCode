class Solution1:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str) -> list[list[str]]:
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) -> None:
        # Base Case
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return
        
        # 单层递归逻辑
        for i in range(start_index, len(s)):
            # 此次比其他组合题目多了一步判断：
            # 判断被截取的这一段子串([start_index, i])是否为回文串
            if self.is_palindrome(s, start_index, i):
                self.path.append(s[start_index:i+1])
                self.backtracking(s, i+1)   # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                self.path.pop()             # 回溯
            else:
                continue    

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start        
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution2:
    def partition(self, s: str) -> list[list[str]]:
        self.isPalindrome = lambda s: s == s[::-1]
        res = []
        self.backtracking(s, res, [])
        return res

    def backtracking(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.backtracking(s[i:], res, path+[s[:i]])
        

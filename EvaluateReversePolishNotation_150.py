class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        func1 = lambda a,b:a+b
        func2 = lambda a,b:a-b
        func3 = lambda a,b:a*b
        func4 = lambda a,b:int(a/b)# 题目要求取整数部份,那么负数的时候是向上取整所以直接int(a/b),不能用b//a
        map = {'+': func1, '-': func2, '*': func3, '/': func4}
        stack = []
        for str in tokens:
            if str in map:
                b = stack.pop()
                a = stack.pop()
                stack.append(map[str](a, b))
            else:
                stack.append(int(str))
        return stack[-1]

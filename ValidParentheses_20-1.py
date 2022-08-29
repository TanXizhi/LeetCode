class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        mapping = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in mapping:
                stack.append(c)
            elif mapping[stack.pop()] != c:
                return False
        return len(stack) == 1

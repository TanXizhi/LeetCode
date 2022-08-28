class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            length = len(ans)
            for i in range(len(ans)):
                temp = ans.pop(0)
                for j in phone[num]:
                    ans.append(''.join([temp, j]))
        return ans

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s if x.isalnum()).lower()
        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in s if x.isalnum()).lower()
        n = len(s)
        left = 0
        right = n-1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

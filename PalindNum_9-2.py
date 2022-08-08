class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = 0
        re = x
        while x > 0:
            ans = ans*10 + x % 10
            x //= 10
        return ans == re

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring
        without repeating characters.
        """
        lst = []
        lenofsub = 0
        for i in range(len(s)):
            while s[i] in lst:
                del lst[0]
            lst.append(s[i])
            lenofsub = max(lenofsub, len(lst))
        return lenofsub

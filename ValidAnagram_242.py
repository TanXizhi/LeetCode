class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26
        for word in s:
            counts[ord(word) - ord('a')] += 1
        for word in t:
            counts[ord(word) - ord('a')] -= 1
        for i in range(26):
            if counts[i] != 0:
                return False
        return True

class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        for i in t:
            if i in s:
                s.remove(i)
            else:
                return False
        if len(s) != 0:
            return False
        else:
            return True


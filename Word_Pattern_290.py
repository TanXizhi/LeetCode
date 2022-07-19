class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        ss = s.split()
        if len(pattern) != len(ss):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict.keys() and ss[i] not in dict.values():
                dict[pattern[i]] = ss[i]
            elif pattern[i] in dict.keys() and dict[pattern[i]] != ss[i]:
                return False
            elif pattern[i] not in dict.keys() and ss[i] in dict.values():
                return False
        return True

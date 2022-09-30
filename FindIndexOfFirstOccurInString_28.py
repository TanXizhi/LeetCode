class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(0, m-n+1):
            p = i
            q = 0
            while q < n and haystack[p] == needle[q]:
                p += 1
                q += 1
            if q == n:
                return i
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(0, m-n+1):
            for j in range(0, n):
                if haystack[i+j] != needle[j]:
                    break
                if j == n-1:
                    return i
        return -1


class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

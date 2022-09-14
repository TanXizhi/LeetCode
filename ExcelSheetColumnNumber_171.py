class Solution1:
    def titleToNumber(self, columnTitle: str) -> int:
        ct = columnTitle[::-1]
        ans = 0
        n = len(ct)
        for i in range(n):
            ans += (ord(ct[i])-ord('A')+1)*26**i
        return ans


class Solution2:
    def titleToNumber(self, columnTitle: str) -> int:
        ct = columnTitle[::-1]
        ans = 0
        power = 1
        for x in ct:
            ans += (ord(x)-64)*power
            power *= 26
        return ans

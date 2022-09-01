class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = (l-len(a))*'0'+a
        b = (l-len(b))*'0'+b
        ans = ''
        carry = 0
        for i in range(l-1, -1, -1):
            num = int(a[i]) + int(b[i]) + carry
            if num >= 2:
                carry = 1
                ans += str(num-2)
            else:
                carry = 0
                ans += str(num)
        if carry == 1:
            ans += '1'
        return ans[::-1]

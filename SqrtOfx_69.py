class Solution1:
    # 二分查找
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


class Solution2:
    # 牛顿迭代法
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        ans = x  # 选择可能的最大值作为初始值是因为迭代是向左的，ans值不断向左迭代趋近于答案。如果选取的初始值较小，可能迭代到另一个负值答案。
        while ans*ans > x:
            ans = 0.5*(ans + x/ans)
        return int(ans)

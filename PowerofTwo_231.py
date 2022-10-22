# 二进制，按位与运算
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0


# 判断是否为最大2的幂的约数
# 根据题目给出的限制：-2^31 <= n <= 2^31 - 1，可知n为32位有符号整数，因此2的幂最小为2^0,最大为2^30，
# 因此只需判断n是否能被2^30整除，即n是否为最大2的幂2^30的约数
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        biggist = 2 ** 30
        return n > 0 and biggist % n == 0

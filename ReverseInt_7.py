class Solution:
    def reverse(self, x: int) -> int:
        upper = 2**31-1
        lower = -2**31

        rev = 0
        while x != 0:
            # lower是负数，整除后向下取整了因此要+1
            if rev < lower//10+1 or rev > upper//10:
                return 0
            digit = x % 10
            # python3中的取模运算在x为负数时会返回[0,9]以内的结果，因此这里需要进行特殊判断处理
            if x < 0 and digit > 0:
                digit -= 10
            # python3的整除是向下取整，在x为负数时会向下取整（更小的负数），因此要先减去尾数digit
            x = (x-digit)//10
            rev = rev*10 + digit
        return rev

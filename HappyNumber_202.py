class Solution1:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total = 0
            while n:     # 从个位开始依次取，平方求和
                n, digit = divmod(n, 10)
                total += digit**2
            return total

        temp = set()  # 初始化一个集合用于存储中间结果
        while True:   # 一直循环直到return
            n = get_next(n)
            if n == 1:
                return True
            elif n in temp:   # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
                return False
            else:
                temp.add(n)   # 如果中间结果既不等于1也不在集合中则将中间结果存储在temp集合中


# 快慢指针法
class Solution2:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total = 0
            while n:     # 从个位开始依次取，平方求和
                n, digit = divmod(n, 10)
                total += digit**2
            return total

        slow_runner = n  # 初始化慢指针为第一个节点
        fast_runner = get_next(n)  # 初始化快指针在第二个节点，即取了一次平方和后的状态
        """
        当慢指针不等于快指针时，慢指针移动一位，快指针移动两位，
        如果链条中有循环则快指针总会追到慢指针（即快指针等于慢指针），进而跳出while循环
        快指针等于慢指针的情况只会有两种，要不都为1，要不快慢指针在链条循环里相遇且这个值肯定不为1
        """
        while slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

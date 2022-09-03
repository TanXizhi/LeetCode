# Fibonacci numbers is the principle behind this problem
# The third number is euqal to the sum of its previous two numbers.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [1, 2]
        for i in range(n-2):
            ways.append(ways[-2] + ways[-1])
        return ways[-1]

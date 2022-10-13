class Solution1:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):  # 原地修改，自底向上每次累加最小的值，最小路径值被存在最上面
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


class Solution2:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if len(triangle) == 0:
            return 0
        # 动态规划 dp表示走到当前位置的时候的最小路径
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:  # 最左边的情况
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:  # 最右边的情况
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])  # 返回最后一层最小的一个

"""
按层模拟

对于每层，从左上方开始以顺时针的顺序遍历所有元素。假设当前层的左上角位于(top,left)，右下角位于(bottom,right)，按照如下顺序遍历当前层的元素。
从左到右遍历上侧元素，依次为(top,left)到(top,right)。
从上到下遍历右侧元素，依次为(top+1,right) 到 (bottom,right)。
如果left<right 且top<bottom，则从右到左遍历下侧元素，依次为(bottom,right−1) 到 (bottom,left+1)，以及从下到上遍历左侧元素，依次为(bottom,left) 到 (top+1,left)。
遍历完当前层的元素之后，将left 和top 分别增加1，将 right 和 bottom 分别减少1，进入下一层继续遍历，直到遍历完所有元素为止。
"""
class Solution1:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        columns = len(matrix[0])
        res = []
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    res.append(matrix[bottom][column])
                for row in range(bottom , top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom -1
        return res


"""
可以模拟螺旋矩阵的路径。初始位置是矩阵的左上角，初始方向是向右，当路径超出界限或者进入之前访问过的位置时，顺时针旋转，进入下一个方向。
判断路径是否进入之前访问过的位置需要使用一个与输入矩阵大小相同的辅助矩阵visited，其中的每个元素表示该位置是否被访问过。
当一个元素被访问时，将visited 中的对应位置的元素设为已访问。
"""
class Solution2:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        columns = len(matrix[0])
        total = rows*columns
        res = [0]*total
        visited = [[False]*columns for _ in range(rows)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        row, column = 0, 0
        for i in range(total):
            res[i] = matrix[row][column]
            visited[row][column] = True
            nextRow = row + directions[directionIndex][0]
            nextColumn = column + directions[directionIndex][1]
            if not (0 <= nextRow <= rows - 1 and 0 <= nextColumn <= columns -1 and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return res

# 将已经走过的地方置None，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向
class Solution3:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        columns = len(matrix[0])
        total = rows*columns
        res = []
        i, j, di, dj = 0, 0, 0, 1
        for _ in range(total):
            res.append(matrix[i][j])
            matrix[i][j] = None
            if not matrix[(i + di) % rows][(j + dj) % columns]:
                di, dj = dj, -di
            i += di
            j += dj
        return res


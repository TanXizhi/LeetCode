from collections import defaultdict

class Solution1:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        x = len(board[0])
        y = len(board)

        # 检查每行
        for i in range(y):
            temp = []
            for j in range(x):
                if board[i][j] == '.':
                    continue
                if board[i][j] in temp:
                    return False
                temp.append(board[i][j])

        # 检查每列
        for j in range(x):
            temp = []
            for i in range(y):
                if board[i][j] == '.':
                    continue
                if board[i][j] in temp:
                    return False
                temp.append(board[i][j])

        # 检查每个九宫格
        for m in range(0, x, 3):  # 3x3每列
            for n in range(0, y, 3):  # 3x3每行
                temp = []
                for i in range(m, m+3):
                    for j in range(n, n+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in temp:
                            return False
                        temp.append(board[i][j])
        return True


class Solution2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 0: row, 1: column, 2: square
        record = {0: defaultdict(set), 1: defaultdict(
            set), 2: defaultdict(set)}
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
                    return False
                # sub-boxes的编号和行列下标的关系
                sb = i // 3 * 3 + j // 3
                if board[i][j] in record[2][sb]:
                    return False
                record[0][i].add(board[i][j])
                record[1][j].add(board[i][j])
                record[2][sb].add(board[i][j])
        return True

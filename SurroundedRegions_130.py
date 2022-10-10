class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board 
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = 'A'
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #判断上下左右相邻的元素是否为‘O‘，进而与边界的’O‘相连通
                temp_i = i + x
                temp_j = j + y
                if 1 <= temp_i < row and 1 <= temp_j < col and board[temp_i][temp_j] == 'O':
                    dfs(temp_i, temp_j)
        
        for i in range(row):
            if board[i][0] == 'O':   #第一列
                dfs(i, 0)
            if board[i][col-1] == 'O':   #最后一列
                dfs(i, col-1)
        
        for j in range(col):
            if board[0][j] == 'O':   #第一行
                dfs(0, j)
            if board[row-1][j] == 'O':   #最后一行
                dfs(row-1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':  #O先变成X，A再变成O
                    board[i][j] = 'X'
                if board[i][j] == 'A':  
                    board[i][j] = 'O'
        return board

    



    


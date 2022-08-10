class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        row = ["" for _ in range(numRows)]
        i = 0
        turn = -1
        for w in s:
            row[i] += w
            if i == 0 or i == numRows - 1:
                turn = - turn
            i += turn
        return "".join(row)

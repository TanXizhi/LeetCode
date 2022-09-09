class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        PT = []
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(PT[i-1][j-1] + PT[i-1][j])
            PT.append(row)
        return PT[-1]


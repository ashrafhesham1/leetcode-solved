class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]
        for i in range(1,rowIndex+1):
            temp = [1]
            for j in range(len(res[-1])-1):
                temp.append(res[-1][j] + res[-1][j+1])
            temp.append(1)
            res.append(temp)

        return res[-1]
        
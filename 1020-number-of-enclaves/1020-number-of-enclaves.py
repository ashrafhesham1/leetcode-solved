class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c) :

            if r not in range(rows) or c not in range(cols): return
            if grid[r][c] == 0 : return

            grid[r][c] = 0

            mr = [0,0,1,-1]
            mc = [1,-1,0,0]

            for i in range(4):
                nr = r + mr[i]
                nc = c + mc[i]

                dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if i in [0, rows-1] or j in [0, cols-1] :
                    if grid[i][j] == 1 :
                        dfs(i,j)

        num = 0
        for i in range(rows):
            for j in range(cols):
                    if grid[i][j] == 1 :
                        num += 1

        return num
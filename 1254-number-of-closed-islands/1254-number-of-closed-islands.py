class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c) :

            if r not in range(rows) or c not in range(cols): return
            if grid[r][c] == 1 : return

            grid[r][c] = 1

            mr = [0,0,1,-1]
            mc = [1,-1,0,0]

            for i in range(4):
                nr = r + mr[i]
                nc = c + mc[i]

                dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if i in [0, rows-1] or j in [0, cols-1] :
                    if grid[i][j] == 0 :
                        dfs(i,j)

        numOfIslands = 0
        for i in range(rows):
            for j in range(cols):
                    if grid[i][j] == 0 :
                        dfs(i,j)
                        numOfIslands += 1

        return numOfIslands
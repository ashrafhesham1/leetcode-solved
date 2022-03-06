class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r,c):
            size = 1
            visited.add((r,c))

            mr = [0,0,1,-1]
            mc = [1,-1,0,0]

            for i in range(4) :
                nr = r + mr[i]
                nc = c + mc[i]

                if nr in range(rows) and nc in range(cols) :
                    if (nr,nc) not in visited and grid[nr][nc] == 1 :
                        size += dfs(nr,nc)
            return size

        for i in range(rows) :
            for j in range(cols) :
                if (i,j) not in visited and grid[i][j] == 1 :
                    maxArea = max(maxArea,dfs(i,j))

        return maxArea
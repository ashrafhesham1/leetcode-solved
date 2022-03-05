class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n=len(grid),len(grid[0])
        res = 0

        visited = [None] * m
        for i in range(len(visited)) : visited[i] = [False] * n

        def dfs(r,c):

            visited[r][c]=True

            mr = [0, 0, 1, -1]
            mc = [1, -1, 0, 0]

            for i in range(4):
                nr = r + mr[i]
                nc = c + mc[i]

                if nr >= 0 and nr < m and nc >= 0 and nc < n :
                        if grid[nr][nc] == '1'  and not visited[nr][nc]:
                             dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1' :
                    dfs(i,j)
                    res += 1

        return res
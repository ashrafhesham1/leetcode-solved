class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or not grid2[r][c] or (r, c) in visited:
                return True

            visited.add((r, c))
    
            res = True
            if not grid1[r][c]:
                res = False
    
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res

            return res

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1
    
        return count
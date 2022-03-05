from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        sr,sc=sr,sc
        m,n=len(image),len(image[0])

        def exploreNeighbours(r,c):
            mr = [0,0,1,-1]
            mc = [1,-1,0,0]

            neighbours = []
            for i in range(4):
                nr = r + mr[i]
                nc = c + mc[i]

                if nr >=0 and nr<m :
                    if nc >=0 and nc<n:
                        neighbours.append([nr,nc])

            return neighbours

        visited = [None] * m
        for i in range(len(visited)) :
            visited[i] = [False] * n

        oldColor = image[sr][sc]

        qr = deque()
        qc = deque()

        qr.append(sr)
        qc.append(sc)
        visited[sr][sc] = True

        while qr :

            r = qr.popleft()
            c = qc.popleft()

            image[r][c] = newColor

            neighbours = exploreNeighbours(r,c)
            for neighbour in neighbours :
                nr = neighbour[0]
                nc = neighbour[1]

                if not visited[nr][nc] and image[nr][nc] == oldColor :
                    visited[nr][nc] = True
                    qr.append(nr)
                    qc.append(nc)


        return image
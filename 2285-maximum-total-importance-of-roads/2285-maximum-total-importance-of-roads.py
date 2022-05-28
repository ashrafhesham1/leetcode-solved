class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        recurs = {}

        def addToRecurs (key) :
            if key in recurs:
                recurs[key] += 1
            else:
                recurs[key] = 1

        for i in range(len(roads)) :
            addToRecurs(roads[i][0])    
            addToRecurs(roads[i][1])    
        
        recurs = dict(sorted(recurs.items(), key = lambda y: y[1], reverse=True))

        importances = [0] * n

        for i in recurs:
            importances[i] = n
            n -= 1

        maxImportance = 0
        for road in roads:
            maxImportance += importances[road[0]] + importances[road[1]]

        return maxImportance
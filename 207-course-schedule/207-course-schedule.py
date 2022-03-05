class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        Map = { i:[] for i in range(numCourses)}
        for i in range(len(prerequisites)) :
            Map[prerequisites[i][0]].append(prerequisites[i][1])
        
        visited = set()
        
        def dfs (course) :
            
            if course in visited : return False
            if Map[course] == [] : return True
            
            visited.add(course)
            for pre in Map[course] :
                if not dfs(pre) : return False
                
            visited.remove(course)
            Map[course] = []
            
            return True
        
        for course in range(numCourses) :
            if not dfs(course) : return False
        
        return True
        
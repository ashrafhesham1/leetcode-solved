class Solution:
    def travel(self,m,n,mpos=0,npos=0,memo={}):
        if mpos == m-1 and npos == n-1 : return 1
        if (mpos,npos) not in memo :
            memo[(mpos,npos)] = (self.travel(m,n,mpos + 1 ,npos,memo) if mpos < m else 0 )+ (self.travel(m,n,mpos,npos+1,memo) if npos < n else 0)
        return memo[mpos,npos]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.travel(m,n,0,0,{})
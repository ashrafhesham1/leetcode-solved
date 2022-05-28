class Solution:
    def digitCount(self, num: str) -> bool:
        num = list(map(int,list(num))) 
        N = len(num) 
        count = [0] * N 
        for i in range(N): 
            cur = num[i] 
            if cur < N :
                count[cur] += 1
            else :
                return False

        if count != num :
            return False
        
        return True
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        arr_str=[None]*numRows
        for i in range(len(arr_str)):
            arr_str[i]=[None]*len(s)
        dir=0
        row,col=0,0
        for i in range(len(s)):
            if dir==0:
                arr_str[row][col]=s[i]
                if row<numRows-1:
                    row+=1
                else:
                    row-=1
                    col+=1
                    dir=1
            else:
                arr_str[row][col]=s[i]
                if row>0:
                    row-=1
                    col+=1
                else:
                    row+=1
                    dir=0
        res=""
        for i in range(len(arr_str)):
            for j in range(len(arr_str[i])):
                if arr_str[i][j]!=None:
                    res+=arr_str[i][j]
        return res
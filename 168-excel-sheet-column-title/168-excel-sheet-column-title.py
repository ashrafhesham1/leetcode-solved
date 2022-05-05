class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while columnNumber > 0 :
            c = chr(ord('A')+ (columnNumber-1) % 26)
            title = c + title
            columnNumber = (columnNumber-1) // 26
        return title
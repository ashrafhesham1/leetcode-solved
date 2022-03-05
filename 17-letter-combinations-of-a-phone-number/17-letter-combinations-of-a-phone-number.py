class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        lettersMap = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}

        res = []
        def makeCombinations(i,curStr):

            if len(curStr) == len(digits) :
                res.append(curStr)
                return

            for char in lettersMap[digits[i]] :
                makeCombinations(i+1,curStr+char)

        if digits :
            makeCombinations(0,"")

        return res
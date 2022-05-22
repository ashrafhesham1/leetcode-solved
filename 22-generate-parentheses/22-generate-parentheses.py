class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        stack = []

        def _generate(open: int, close: int):

            if open == close == n :
                res.append("".join(stack))
                return

            if open < n :
                stack.append('(')
                _generate(open + 1, close)
                stack.pop()

            if open > close :
                stack.append(')')
                _generate(open, close + 1)
                stack.pop()

        _generate(0,0)
        return res

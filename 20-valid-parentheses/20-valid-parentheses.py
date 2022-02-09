class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        swich={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in range(len(s)):
            if s[i] in swich.keys():
                stack.append(s[i])
            else :
                if len(stack)>0 and  s[i]==swich[stack.pop()]:
                    pass
                else:
                    return False
        return not len(stack)
                
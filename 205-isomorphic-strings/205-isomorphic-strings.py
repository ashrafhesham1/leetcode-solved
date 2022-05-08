class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        occurs = {}
        for i in range(len(s)):
            if s[i] in occurs :
                if occurs[s[i]] != t[i] : return False
            else:
                if t[i]  in occurs.values() :return False
                occurs[s[i]] = t[i]
        return True
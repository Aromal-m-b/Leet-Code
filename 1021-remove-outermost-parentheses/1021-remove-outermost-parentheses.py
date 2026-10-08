class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0
        start = 0
        for i in range(len(s)):
            if '(' == s[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                res = res + s[start+1 :  i] 
                start = i+1
        return res
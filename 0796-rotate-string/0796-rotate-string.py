class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ind = False
        occu = []
        i = 0 
        while i < len(goal) and s[0] in goal[i:]:
            if goal[i]  == s[0]:
                if s == goal[i:] + goal[:i]:
                    ind = True
            i += 1
        return ind
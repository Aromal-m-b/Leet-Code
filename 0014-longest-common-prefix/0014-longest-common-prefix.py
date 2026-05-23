class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        temp = strs[0]
        limit = len(temp)
        while limit > 0:
            for i in range(1,len(strs)):
                for j in range(0,limit):
                    if  j == len(strs[i]):
                        limit = j
                        break
                    if temp[j] != strs[i][j]:
                        limit = j
                        break
            return temp[0:limit]
        return ""
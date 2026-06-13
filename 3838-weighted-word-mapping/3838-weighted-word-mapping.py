class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        code = 122
        rev_map = {}
        weight_map = {}
        for i in range(26):
            rev_map[i] = chr(code)
            weight_map[chr(219-code)] = weights[i]  
            code -= 1
        res = ""
        for i in words:
            weight = 0 
            for j in i:
                weight += weight_map[j]
            res = res + rev_map[weight%26]
        return res
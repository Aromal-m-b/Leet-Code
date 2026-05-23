class Solution:
    def romanToInt(self, s: str) -> int:
        temp = s[0]
        
        hmap = {
            'O':[0,'Z'],
            'I':[1,'O'],
            'V':[5,'I'],
            'X':[10,'I'],
            'L':[50,'X'],
            'C':[100,'X'],
            'D':[500,'C'],
            'M':[1000,'C'],
        }
        res = 0
        res += hmap[temp][0]
        for i in range(1,len(s)):
            if temp == hmap[s[i]][1]:
                res -= hmap[temp][0]
                res += hmap[s[i]][0] - hmap[temp][0]
            else:
                res += hmap[s[i]][0]
                temp = s[i]

        return res
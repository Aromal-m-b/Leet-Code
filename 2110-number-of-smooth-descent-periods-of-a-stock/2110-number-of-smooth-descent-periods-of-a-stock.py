class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = len(prices)
        c = 0
        for i in range (1,len(prices)):
            if prices[i-1] == prices[i]+1:
                c += 1
            else:
                if c==0:
                    continue
                res += int(((c*(c+1))/2))
                c = 0
        if c!=0:
            res += (int(((c*(c+1))/2)))
            c = 0
        return res
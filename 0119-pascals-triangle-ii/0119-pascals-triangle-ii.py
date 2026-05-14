class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        rowIndex+=1
        if rowIndex == 1:
            return res
        for i in range(1,rowIndex):
            curr = []
            curr.append(res[0])
            j = 1
            while j < len(res) :
                curr.append(res[j-1]+res[j])
                j+=1
            curr.append(res[-1])
            res = curr
        return res
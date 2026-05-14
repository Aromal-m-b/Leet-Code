class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            j = 1
            limit = len(res[i-1])
            curr = [1]
            while j<limit:
                curr.append(res[i-1][j-1]+res[i-1][j])
                j+=1
            curr.append(1)
            res.append(curr)

        return res

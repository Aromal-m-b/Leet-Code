class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix = set()
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i] in prefix:
                cnt += 1
            else:
                prefix.add(A[i])
            if B[i] in prefix:
                cnt+=1
            else:
                prefix.add(B[i])
            res.append(cnt)
        return res
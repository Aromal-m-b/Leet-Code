class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix = set()
        prefix.add(A[0])
        prefix.add(B[0])
        res = []
        res.append(2 - len(prefix))
        if len(A)>1:
            for i in range(1,len(A)):
                prefix.add(A[i])
                prefix.add(B[i])
                res.append((2*(i+1))-len(prefix))
                # print(prefix)
        return res
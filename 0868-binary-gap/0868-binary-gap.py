class Solution:
    def binaryGap(self, n: int) -> int:
        curr = 0
        prev = -1
        result = 0
        while n>0:
            if(n&1) > 0:
                result = max(result,curr-prev) if prev!= -1 else result
                prev = curr
            curr+=1
            n >>= 1
        return result

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        res = []
        for n in nums:
            if n != val:
                res.append(n)
                cnt+=1
        nums[:] = res
        return cnt
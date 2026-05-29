class Solution:
    def minElement(self, nums: List[int]) -> int:
        val = 10 ** 4
        for i in range (len(nums)):
            res = 0
            for c in str(nums[i]):
                res = res + int(c)
            val = min(res,val)
            if val == 1:
                return val
        return val
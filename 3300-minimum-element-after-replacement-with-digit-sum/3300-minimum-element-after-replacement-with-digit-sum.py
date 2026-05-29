class Solution:
    def minElement(self, nums: List[int]) -> int:
        val = 10 ** 4
        for i in range (len(nums)):
            temp  = str(nums[i])
            res = 0
            for c in temp:
                res = res + int(c)
            val = min(res,val)
        return val
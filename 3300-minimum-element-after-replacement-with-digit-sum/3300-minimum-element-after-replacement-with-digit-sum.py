class Solution:
    def minElement(self, nums: List[int]) -> int:
        val = 10 ** 4
        for i in range (len(nums)):
            val = min(val,sum(map(int,str(nums[i]))))
        return val
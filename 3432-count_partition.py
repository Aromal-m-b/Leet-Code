class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum (nums)
        c = 0
        for i in range(0,len(nums)-1):
            l = sum(nums[0:i])
            if abs((l-(s-l)))%2 == 0:
                c = c + 1
        return c

class Solution:
    def check(self, nums: List[int]) -> bool:
        peak = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                peak += 1
            if peak>1:
                return False
        return True
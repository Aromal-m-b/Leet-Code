class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        curr = 0
        res = []
        cumulate = sum(nums)
        for i in range(0,len(nums)):
            left = curr
            curr += nums[i]
            right = cumulate - curr
            res.append(abs(right-left))
        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 0
        temp = 0
        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                temp += 1
            else:
                count = max(count,temp)
                temp = 0
        count = max(temp,count)
        return count+1